"""
Inicializa y migra la base de datos SQLite.
"""

from database.models import Base

def initialize_database(engine):
    """Crea todas las tablas en la base de datos si aún no existen."""
    Base.metadata.create_all(engine) 