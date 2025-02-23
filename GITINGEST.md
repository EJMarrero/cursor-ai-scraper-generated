================================================
File: README.md
================================================
# Proyecto de Análisis de Sentimientos

Este proyecto es una solución full-stack que realiza análisis de sentimientos usando Web Scraping, la API de OpenAI y almacenamiento en una base de datos SQLite. Además, expone una API REST usando Flask y muestra los datos en un frontend implementado con Vue 3, Vite y TypeScript, siguiendo un patrón repositorio en la capa de servicios.

## Arquitectura y Módulos

- **Scraper**  
  - `scraper_analysis.py`: Realiza scraping de opiniones, análisis de sentimiento y guarda los resultados.
  - `twitter_trends_scraper.py`: Extrae trending topics desde Trends24.

- **Database**  
  - `init_db.py`: Inicializa y migra la base de datos SQLite.
  - `models.py`: Define los modelos de datos (Opiniones y Trending).

- **Backend**  
  - `api_app.py`: Aplicación Flask con endpoints:
    - `/`: Mensaje de bienvenida.
    - `/api/opiniones`: Retorna opiniones analizadas.
    - `/api/trending`: Retorna trending topics.
  - `config.py`: Configuraciones de la aplicación.
  - `blueprints/`: Contiene los endpoints modularizados.
  - `tests/`: Pruebas unitarias e integración para el backend (con pytest).

- **Frontend**  
  - Implementado con Vue 3, Vite y TypeScript.
  - Estructura:
    - `components/`: Componentes reutilizables (ReviewCard, TrendingCard).
    - `views/`: Vistas principales (HomeView).
    - `store/`: Gestión de estado global con Pinia.
    - `services/`: Capa repositorio para llamadas al backend.
    - `models/`: Definición de interfaces y tipos.

## Configuración del Entorno

1. **Variables de entorno**  
   Crea un archivo `.env` basado en `.env.example`:

   ```dotenv
   OPENAI_API_KEY=tu_openai_api_key_aqui
   DATABASE_URL=sqlite:///database.db
   VITE_API_URL=http://localhost:3000/api
   ```

2. **Backend**  
   - Instalar dependencias: `pip install -r requirements.txt`
   - Ejecutar la aplicación: `python backend/api_app.py`

3. **Scraper**  
   - Ejecutar el scraper de opiniones: `python scraper/scraper_analysis.py`
   - Ejecutar el scraper de trending topics: `python scraper/twitter_trends_scraper.py`

4. **Frontend**  
   - Navegar a la carpeta `frontend` y ejecutar:
     ```bash
     npm install
     npm run dev
     ```

## Testing y CI/CD

- Se incluyen pruebas unitarias para el backend en `backend/tests/`.
- Se incluye una prueba end-to-end en `tests/e2e/spec.cy.ts` para el frontend (usando Cypress).
- Un pipeline de CI/CD está configurado en `.github/workflows/ci.yml`.

## Despliegue

Se incluye ejemplo de despliegue con Docker y Docker Compose:
- `Dockerfile`: Para el backend.
- `docker-compose.yml`: Para levantar backend y frontend en contenedores.

## Contribución y Convenciones

- Se emplean buenas prácticas de desarrollo, logging y manejo de errores.
- Documentación y comentarios en cada módulo.
- Se utilizan herramientas de linting (Black, ESLint/Prettier) para garantizar la calidad del código.

---

¡Disfruta desarrollando y ampliando esta solución! 

================================================
File: Dockerfile
================================================
# Utilizamos una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el contenido del proyecto
COPY . /app

# Instalar dependencias de Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exponer el puerto 5000 para Flask
EXPOSE 5000

# Comando para iniciar el backend
CMD ["python", "backend/api_app.py"] 

================================================
File: LICENSE
================================================
MIT License

Copyright (c) 2025 EJMarrero

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


================================================
File: alembic.ini
================================================
# A generic, single database configuration.

[alembic]
# path to migration scripts
# Use forward slashes (/) also on windows to provide an os agnostic path
script_location = alembic

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# see https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file
# for all available tokens
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.
prepend_sys_path = .

# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the python>=3.9 or backports.zoneinfo library and tzdata library.
# Any required deps can installed by adding `alembic[tz]` to the pip requirements
# string value is passed to ZoneInfo()
# leave blank for localtime
# timezone =

# max length of characters to apply to the "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to alembic/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "version_path_separator" below.
# version_locations = %(here)s/bar:%(here)s/bat:alembic/versions

# version path separator; As mentioned above, this is the character used to split
# version_locations. The default within new alembic.ini files is "os", which uses os.pathsep.
# If this key is omitted entirely, it falls back to the legacy behavior of splitting on spaces and/or commas.
# Valid values for version_path_separator are:
#
# version_path_separator = :
# version_path_separator = ;
# version_path_separator = space
# version_path_separator = newline
#
# Use os.pathsep. Default configuration used for new projects.
version_path_separator = os

# set to 'true' to search source files recursively
# in each "version_locations" directory
# new in Alembic version 1.10
# recursive_version_locations = false

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

sqlalchemy.url = sqlite:///database.db


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the exec runner, execute a binary
# hooks = ruff
# ruff.type = exec
# ruff.executable = %(here)s/.venv/bin/ruff
# ruff.options = --fix REVISION_SCRIPT_FILENAME

# Logging configuration
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine
propagate = 0

[logger_alembic]
level = INFO
handlers =
qualname = alembic
propagate = 0

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S


================================================
File: docker-compose.yml
================================================
version: "3.8"
services:
  backend:
    build: .
    container_name: sentiment_backend
    ports:
      - "5000:5000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - DATABASE_URL=${DATABASE_URL}
  frontend:
    image: node:16-alpine
    working_dir: /app
    volumes:
      - ./frontend:/app
    command: sh -c "npm install && npm run dev"
    ports:
      - "3000:3000" 

================================================
File: package.json
================================================
{
  "dependencies": {
    "cors": "^2.8.5",
    "vue": "^3.5.13"
  },
  "devDependencies": {
    "@types/node": "^22.13.5",
    "@vitejs/plugin-vue": "^5.2.1",
    "autoprefixer": "^10.4.20",
    "cypress": "^14.0.3",
    "postcss": "^8.5.3",
    "tailwindcss": "^4.0.8"
  }
}


================================================
File: requirements.txt
================================================
Flask==2.3.2
Werkzeug>=2.0,<3.0
Flask-Cors==3.0.10
SQLAlchemy==1.4.47
requests==2.28.2
beautifulsoup4==4.12.2
openai==0.27.8
python-dotenv==1.0.0
pytest==7.2.0
pytest-flask==1.2.0
alembic==1.11.1

================================================
File: tsconfig.json
================================================
{
  "compilerOptions": {
    "types": ["cypress", "node"],
    "skipLibCheck": true
  }
} 

================================================
File: vite.config.ts
================================================
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  server: {
    host: 'localhost',
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        localAddress: '127.0.0.1'
      },
    },
  },
});


================================================
File: alembic/README
================================================
Generic single-database configuration.

================================================
File: alembic/env.py
================================================
import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Agrega el directorio raíz al path para poder importar el módulo database
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Importa el metadata de los modelos
from database.models import Base  # Asegúrate de que este import funcione

# Define el metadata como target para las migraciones
target_metadata = Base.metadata

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()


================================================
File: alembic/script.py.mako
================================================
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    ${downgrades if downgrades else "pass"}


================================================
File: alembic/versions/ececb794b78b_add_url_column_to_trending_model.py
================================================
"""Add url column to Trending model

Revision ID: ececb794b78b
Revises: 
Create Date: 2025-02-22 22:35:08.484357

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ececb794b78b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trending', sa.Column('url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('trending', 'url')
    # ### end Alembic commands ###


================================================
File: backend/api_app.py
================================================
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
# Esta configuración permite solicitudes solo desde http://localhost:3000 para rutas que coincidan con /api/*
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Registrar blueprints
from backend.blueprints.opiniones import opiniones_bp
from backend.blueprints.trending import trending_bp

app.register_blueprint(opiniones_bp, url_prefix="/api/opiniones")
app.register_blueprint(trending_bp, url_prefix="/api/trending")

@app.route("/")
def index():
    """
    Endpoint raíz con un mensaje de bienvenida.
    """
    return jsonify({
        "mensaje": "Bienvenido al API de Análisis de Sentimientos.",
        "rutas": {
            "/api/opiniones": "Obtiene opiniones analizadas.",
            "/api/trending": "Obtiene trending topics."
        }
    })

# Manejo global de errores
@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Error: {e}")
    return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000) 

================================================
File: backend/config.py
================================================
"""
Configuración del backend.
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False 

================================================
File: backend/server.js
================================================
const express = require('express');
const cors = require('cors');

const app = express();

// Permitir peticiones CORS para todas las rutas y métodos
app.use(cors());
// Manejar solicitudes preflight (OPTIONS)
app.options('*', cors());

// Rutas de tu API
app.get('/api/opiniones', (req, res) => {
  res.json({ message: 'Opiniones' });
});

// Otras rutas...

app.listen(5000, () => console.log('Servidor iniciado en el puerto 5000')); 

================================================
File: backend/blueprints/opiniones.py
================================================
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
    """
    Retorna todas las opiniones analizadas.
    """
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

================================================
File: backend/blueprints/trending.py
================================================
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
    """
    Retorna los trending topics extraídos.
    """
    session = Session()
    try:
        # Ejecuta el scraper y actualiza los trending topics independientemente de los registros existentes
        topics = scrape_trending_topics()
        # Elimina los registros existentes
        session.query(Trending).delete()
        # Inserta los trending topics extraídos
        for topic in topics:
            nuevo_trend = Trending(topic=topic["topic"], url=topic["url"], obtenido_en=datetime.utcnow())
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

================================================
File: backend/tests/test_api.py
================================================
"""
Pruebas unitarias e integración para la API usando pytest.
"""

import pytest
from backend.api_app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Prueba del endpoint raíz."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert "mensaje" in data

def test_get_opiniones(client):
    """Prueba del endpoint de opiniones."""
    response = client.get("/api/opiniones/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_get_trending(client):
    """Prueba del endpoint de trending topics."""
    response = client.get("/api/trending/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list) 

================================================
File: database/init_db.py
================================================
"""
Inicializa y migra la base de datos SQLite.
"""

from database.models import Base

def initialize_database(engine):
    """
    Crea todas las tablas en la base de datos si aún no existen.
    """
    Base.metadata.create_all(engine) 

================================================
File: database/models.py
================================================
"""
Definición de modelos para la base de datos utilizando SQLAlchemy.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func

Base = declarative_base()

class Opinion(Base):
    """
    Modelo para almacenar opiniones y su análisis de sentimiento.
    """
    __tablename__ = "opiniones"
    id = Column(Integer, primary_key=True, index=True)
    texto = Column(String, nullable=False)
    sentimiento = Column(String, nullable=False)
    creado_en = Column(DateTime, server_default=func.now())

class Trending(Base):
    """
    Modelo para almacenar trending topics.
    """
    __tablename__ = "trending"
    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, nullable=False)
    url = Column(String, nullable=True)
    obtenido_en = Column(DateTime, server_default=func.now()) 

================================================
File: frontend/index.css
================================================
@tailwind base;
@tailwind components;
@tailwind utilities; 

================================================
File: frontend/index.html
================================================
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <title>Aplicación Vue TypeScript</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <body>
    <!-- Contenedor donde se monta la aplicación Vue -->
    <div id="app"></div>
    <!-- Se carga el módulo main.ts; el bundler (por ejemplo, Vite) se encargará de compilarlo -->
    <script type="module" src="/src/main.ts"></script>
  </body>
</html> 

================================================
File: frontend/package.json
================================================
{
  "name": "sentiment-frontend",
  "version": "1.0.0",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "lint": "eslint --ext .ts,.vue src",
    "test": "vitest"
  },
  "dependencies": {
    "vue": "^3.2.0",
    "pinia": "^2.0.0",
    "axios": "^0.27.2"
  },
  "devDependencies": {
    "typescript": "^4.5.0",
    "vite": "^2.9.0",
    "@vitejs/plugin-vue": "^2.0.0",
    "eslint": "^8.0.0",
    "eslint-plugin-vue": "^8.0.0",
    "tailwindcss": "^3.0.0",
    "postcss": "^8.0.0",
    "autoprefixer": "^10.0.0",
    "vitest": "^0.0.118"
  }
}

================================================
File: frontend/postcss.config.js
================================================
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
} 

================================================
File: frontend/tailwind.config.js
================================================
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
} 

================================================
File: frontend/tsconfig.json
================================================
{
  "compilerOptions": {
    "target": "esnext",
    "useDefineForClassFields": true,
    "module": "esnext",
    "moduleResolution": "node",
    "strict": true,
    "jsx": "preserve",
    "sourceMap": true,
    "resolveJsonModule": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "lib": ["ESNext", "DOM"],
    "types": ["vite/client", "node"]
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
} 

================================================
File: frontend/vite.config.ts
================================================
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// Configuración de Vite con proxy para el backend
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        /* rewrite: (path) => path.replace(/^\/api/, '/api') */
      }
    }
  }
}) 

================================================
File: frontend/public/index.html
================================================
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <title>Proyecto de Análisis de Sentimientos</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script type="module" src="/src/main.ts"></script>
  </head>
  <body>
    <div id="app"></div>
  </body>
</html> 

================================================
File: frontend/src/App.vue
================================================
<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">Análisis de Sentimientos</h1>
    <!-- Se despliega la vista principal -->
    <HomeView />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import HomeView from './views/HomeView.vue'

export default defineComponent({
  name: 'App',
  components: { HomeView }
})
</script>

<style>
/* Estilos globales personalizados */
</style> 

================================================
File: frontend/src/main.ts
================================================
import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import '../index.css' // Actualizado para buscar index.css en la carpeta superior

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.mount('#app') 

================================================
File: frontend/src/shims-vue.d.ts
================================================
declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
} 

================================================
File: frontend/src/components/ReviewCard.vue
================================================
<template>
  <div class="bg-white shadow-md rounded p-4 mb-4">
    <p class="text-gray-700">{{ opinion.texto }}</p>
    <p class="text-sm text-gray-500 mt-2">Sentimiento: {{ opinion.sentimiento }}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'
import { Opinion } from '../models/Opinion'

export default defineComponent({
  name: 'ReviewCard',
  props: {
    opinion: {
      type: Object as PropType<Opinion>,
      required: true
    }
  }
})
</script> 

================================================
File: frontend/src/components/TrendingCard.vue
================================================
<template>
  <div class="bg-blue-100 shadow-md rounded p-4 mb-4">
    <a :href="trending.url" target="_blank" class="text-blue-800 font-semibold hover:underline">
      {{ trending.topic }}
    </a>
    <p class="text-xs text-blue-600 mt-1">Obtenido: {{ trending.obtenido_en }}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'
import { Trending } from '../models/Trending'

export default defineComponent({
  name: 'TrendingCard',
  props: {
    trending: {
      type: Object as PropType<Trending>,
      required: true
    }
  }
})
</script> 

================================================
File: frontend/src/models/Opinion.ts
================================================
export interface Opinion {
  id: number
  texto: string
  sentimiento: string
  creado_en: string
} 

================================================
File: frontend/src/models/Trending.ts
================================================
export interface Trending {
  id: number
  topic: string
  url: string
  obtenido_en: string
} 

================================================
File: frontend/src/services/apiService.ts
================================================
import axios from 'axios'
import { Opinion } from '../models/Opinion'
import { Trending } from '../models/Trending'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:3000/api'

export default {
  async getOpiniones(): Promise<Opinion[]> {
    try {
      const response = await axios.get(`${API_URL}/opiniones`)
      return response.data
    } catch (error) {
      console.error('Error al obtener opiniones:', error)
      return []
    }
  },
  async getTrending(): Promise<Trending[]> {
    try {
      const response = await axios.get(`${API_URL}/trending`)
      return response.data
    } catch (error) {
      console.error('Error al obtener trending topics:', error)
      return []
    }
  }
} 

================================================
File: frontend/src/store/index.ts
================================================
import { defineStore } from 'pinia'
import apiService from '../services/apiService'
import { Opinion } from '../models/Opinion'
import { Trending } from '../models/Trending'

export const useDataStore = defineStore('dataStore', {
  state: () => ({
    opiniones: [] as Opinion[],
    trending: [] as Trending[]
  }),
  actions: {
    async fetchOpiniones() {
      this.opiniones = await apiService.getOpiniones()
    },
    async fetchTrending() {
      this.trending = await apiService.getTrending()
    }
  }
}) 

================================================
File: frontend/src/views/HomeView.vue
================================================
<template>
  <div>
    <h2 class="text-2xl font-bold mb-2">Opiniones Analizadas</h2>
    <div v-if="opiniones.length === 0">Cargando opiniones...</div>
    <ReviewCard v-for="op in opiniones" :key="op.id" :opinion="op" />
    
    <h2 class="text-2xl font-bold mt-8 mb-2">Trending Topics</h2>
    <div v-if="trendingList.length === 0">Cargando trending topics...</div>
    <TrendingCard v-for="trend in trendingList" :key="trend.id" :trending="trend" />
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import ReviewCard from '../components/ReviewCard.vue'
import TrendingCard from '../components/TrendingCard.vue'
import apiService from '../services/apiService'
import { Opinion } from '../models/Opinion'
import { Trending } from '../models/Trending'

export default defineComponent({
  name: 'HomeView',
  components: {
    ReviewCard,
    TrendingCard
  },
  setup() {
    const opiniones = ref<Opinion[]>([])
    const trendingList = ref<Trending[]>([])

    const cargarDatos = async () => {
      try {
        opiniones.value = await apiService.getOpiniones()
        trendingList.value = await apiService.getTrending()
      } catch (error) {
        console.error("Error al cargar los datos", error)
      }
    }

    onMounted(() => {
      cargarDatos()
    })

    return { opiniones, trendingList }
  }
})
</script> 

================================================
File: scraper/scraper_analysis.py
================================================
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
        # Ajustar el selector de acuerdo a la estructura de la página
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
    Deberá devolver una palabra: "positivo", "negativo" o "neutral".
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
    # Configurar la conexión a la base de datos
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Inicializar la base de datos (crea tablas si no existen)
    init_db.initialize_database(engine)

    # Obtener opiniones vía scraping
    opiniones = scrape_opinions()
    for opinion_text in opiniones:
        sentimiento = analizar_sentimiento(opinion_text)
        guardar_opinion(session, opinion_text, sentimiento)

if __name__ == "__main__":
    main() 

================================================
File: scraper/twitter_trends_scraper.py
================================================
"""
Script para realizar el scraping de trending topics usando Requests y BeautifulSoup.
Basado en Trends24.
"""

import logging
import requests
from bs4 import BeautifulSoup

# Configurar logging
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

        # Buscar el contenedor <ol> que contiene la lista de trending topics
        lista = soup.find("ol", class_="trend-card__list")
        if not lista:
            logger.error("No se encontró la lista de trending topics.")
            return []

        # Iterar sobre cada elemento <li> en el contenedor e extraer el texto y el href
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

================================================
File: src/shims-vue.d.ts
================================================
declare module '*.vue' {
  import { DefineComponent } from 'vue'
  export default {} as DefineComponent<{}, {}, any>
} 

================================================
File: tests/e2e/spec.cy.ts
================================================
/// <reference types="cypress" />

describe('Prueba End-to-End del Frontend', () => {
  it('Debe cargar la página principal y mostrar opiniones y trending topics', () => {
    cy.visit('http://localhost:3000')
    cy.contains('Análisis de Sentimientos')
    // Verificar la existencia de tarjetas (asumiendo que los componentes tienen clases distintivas)
    cy.get('.ReviewCard, .TrendingCard').should('exist')
  })
}) 

================================================
File: .github/workflows/ci.yml
================================================
name: CI Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  backend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Instalar dependencias
        run: pip install -r requirements.txt
      - name: Ejecutar tests de backend
        run: pytest --maxfail=1 --disable-warnings -q

  frontend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Configurar Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '16'
      - name: Instalar dependencias y ejecutar linter/test
        working-directory: ./frontend
        run: |
          npm install
          npm run lint
          npm run test 

