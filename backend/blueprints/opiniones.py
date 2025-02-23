"""
Blueprint que expone el endpoint /api/opiniones.
"""

import os
from flask import Blueprint, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Opinion

opiniones_bp = Blueprint("opiniones_bp", __name__)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@opiniones_bp.route("/", methods=["GET"])
def get_opiniones():
    """Retorna todas las opiniones analizadas."""
    session = Session()
    try:
        opiniones = session.query(Opinion).all()
        result = []
        for opinion in opiniones:
            result.append({
                "id": opinion.id,
                "texto": opinion.texto,
                "sentimiento": opinion.sentimiento,
                "creado_en": opinion.creado_en.isoformat()
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close() 