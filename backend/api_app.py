"""
Aplicación Flask que expone la API REST con manejo de errores, logging y CORS.
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS
from backend.config import DevelopmentConfig
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
# Permitir solicitudes solo desde http://localhost:3000 para rutas /api/*
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Registrar blueprints
from backend.blueprints.opiniones import opiniones_bp
from backend.blueprints.trending import trending_bp

app.register_blueprint(opiniones_bp, url_prefix="/api/opiniones")
app.register_blueprint(trending_bp, url_prefix="/api/trending")

@app.route("/")
def index():
    """Endpoint raíz con un mensaje de bienvenida."""
    return jsonify({
        "mensaje": "Bienvenido al API de Análisis de Sentimientos.",
        "rutas": {
            "/api/opiniones": "Obtiene opiniones analizadas.",
            "/api/trending": "Obtiene trending topics."
        }
    })

@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Error: {e}")
    return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000) 