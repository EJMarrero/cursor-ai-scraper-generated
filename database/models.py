"""
Definición de modelos para la base de datos utilizando SQLAlchemy.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func

Base = declarative_base()

class Opinion(Base):
    """Modelo para almacenar opiniones y su análisis de sentimiento."""
    __tablename__ = "opiniones"
    id = Column(Integer, primary_key=True, index=True)
    texto = Column(String, nullable=False)
    sentimiento = Column(String, nullable=False)
    creado_en = Column(DateTime, server_default=func.now())

class Trending(Base):
    """Modelo para almacenar trending topics."""
    __tablename__ = "trending"
    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, nullable=False)
    url = Column(String, nullable=True)
    obtenido_en = Column(DateTime, server_default=func.now()) 