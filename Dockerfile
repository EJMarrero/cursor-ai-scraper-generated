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