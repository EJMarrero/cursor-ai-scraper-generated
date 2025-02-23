"""
Blueprint que expone el endpoint /api/trending.
"""

import os
from flask import Blueprint, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Trending
from datetime import datetime
from scraper.twitter_trends_scraper import scrape_trending_topics

trending_bp = Blueprint("trending_bp", __name__)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@trending_bp.route("/", methods=["GET"], strict_slashes=False)
def get_trending():
    """Retorna los trending topics extraídos."""
    session = Session()
    try:
        topics = scrape_trending_topics()
        session.query(Trending).delete()
        for topic in topics:
            nuevo_trend = Trending(
                topic=topic["topic"],
                url=topic["url"],
                obtenido_en=datetime.utcnow()
            )
            session.add(nuevo_trend)
        session.commit()
        trending_list = session.query(Trending).all()
        result = []
        for trend in trending_list:
            result.append({
                "id": trend.id,
                "topic": trend.topic,
                "url": trend.url,
                "obtenido_en": trend.obtenido_en.isoformat()
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close() 