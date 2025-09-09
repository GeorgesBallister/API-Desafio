FROM python:3.9-slim

WORKDIR /app

COPY . .

# Porta
EXPOSE 5000

# Instalar as dependencias
RUN pip install -r requirements.txt

# API vai rodar esse comando toda vez que o docker iniciar
CMD ["python", "app.py"]