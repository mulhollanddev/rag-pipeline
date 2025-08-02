# Dockerfile otimizado
FROM python:3.10-slim-buster

WORKDIR /app

# Dependências do sistema (caso precise)
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Exponha a porta apenas se necessário
# EXPOSE 8000

# Comando padrão para rodar o app
CMD ["python", "rag_app.py"]
