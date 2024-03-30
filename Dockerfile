# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o código-fonte para o contêiner
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir fastapi uvicorn[standard]

# Exponha a porta 8000
EXPOSE 8000

# Comando para executar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
