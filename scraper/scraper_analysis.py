"""
Script para realizar el scraping de opiniones, analizar el sentimiento usando la API de OpenAI
y guardar los resultados en la base de datos SQLite.
"""

import os
import logging
import requests
import openai
from bs4 import BeautifulSoup
from database import init_db
from database.models import Opinion
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")
openai.api_key = OPENAI_API_KEY

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_opinions():
    """
    Realiza el scraping de opiniones desde una página web.
    Aquí se usa una URL de ejemplo; reemplazar por la fuente real.
    """
    url = "http://quotes.toscrape.com/"  # URL ejemplo
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        opinion_elements = soup.select(".quote span.text")
        opiniones = [elem.get_text(strip=True) for elem in opinion_elements]
        logger.info(f"Se encontraron {len(opiniones)} opiniones.")
        return opiniones
    except Exception as e:
        logger.error(f"Error en scraping de opiniones: {e}")
        return []

def analizar_sentimiento(texto):
    """
    Analiza el sentimiento de un texto usando el modelo GPT-3.5-turbo a través del endpoint de Chat.
    Debe devolver: "positivo", "negativo" o "neutral".
    """
    messages = [
        {"role": "system", "content": "Eres un analizador de sentimientos. Debes evaluar un texto y devolver solamente una palabra: positivo, negativo o neutral."},
        {"role": "user", "content": f"Analiza el sentimiento del siguiente texto:\n\n\"{texto}\""}
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=60,
            temperature=0.7
        )
        resultado = response.choices[0].message.content.strip().lower()
        logger.info(f"Opinión analizada: {texto[:30]}... Sentimiento: {resultado}")
        return resultado
    except Exception as e:
        logger.error(f"Error en análisis de sentimiento: {e}")
        return "desconocido"

def guardar_opinion(session, texto, sentimiento):
    """
    Guarda la opinión y su sentimiento en la base de datos.
    """
    opinion = Opinion(texto=texto, sentimiento=sentimiento)
    session.add(opinion)
    session.commit()
    logger.info("Opinión guardada en la base de datos.")

def main():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    init_db.initialize_database(engine)

    opiniones = scrape_opinions()
    for opinion_text in opiniones:
        sentimiento = analizar_sentimiento(opinion_text)
        guardar_opinion(session, opinion_text, sentimiento)

if __name__ == "__main__":
    main() 