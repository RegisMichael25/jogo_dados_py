# 1. Escolha uma imagem base oficial do Python. A versão "slim" é mais leve.
FROM python:3.11-slim

# 2. Defina o diretório de trabalho dentro do contêiner.
WORKDIR /app

# 3. Copie o arquivo de dependências para dentro do contêiner.
COPY requirements.txt .

# 4. Instale as dependências. Usar --no-cache-dir deixa a imagem menor.
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copie o código-fonte do seu projeto (a pasta 'src') para o diretório de trabalho no contêiner.
COPY ./src .

# 6. Comando que será executado quando o contêiner iniciar.
# Ele vai rodar o arquivo principal do seu jogo.
CMD ["python", "main.py"]