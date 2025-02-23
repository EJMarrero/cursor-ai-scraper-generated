"""
Script para realizar el scraping de trending topics usando Requests y BeautifulSoup.
Basado en Trends24.
"""

import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_trending_topics():
    """
    Obtiene trending topics desde Trends24 usando encabezados apropiados y
    buscando el contenedor <ol> principal.
    """
    url = "https://trends24.in/"
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/91.0.4472.124 Safari/537.36"),
        "Referer": "https://trends24.in/"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        lista = soup.find("ol", class_="trend-card__list")
        if not lista:
            logger.error("No se encontró la lista de trending topics.")
            return []
        items = lista.find_all("li")
        trends = []
        for item in items:
            a_tag = item.find("a", href=True)
            if a_tag:
                topic_text = a_tag.get_text(strip=True)
                link_href = a_tag.get("href")
                trends.append({"topic": topic_text, "url": link_href})
        logger.info(f"Se encontraron {len(trends)} trending topics.")
        return trends
    except Exception as e:
        logger.error(f"Error en scraping de trending topics: {e}")
        return []

if __name__ == "__main__":
    trending = scrape_trending_topics()
    for topic in trending:
        print(topic) 