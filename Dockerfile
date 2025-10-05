# Dockerfile

# Usa uma versão segura e recente do Python
FROM python:3.11-slim-bookworm

# Cria um usuário não-root para segurança
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Define o diretório de trabalho e copia os arquivos de dependência
WORKDIR /app
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código e muda a propriedade para o novo usuário
COPY . .
RUN chown -R appuser:appuser /app

# Muda para o usuário não-root
USER appuser

# Comando ATUALIZADO para rodar a aplicação em modo "unbuffered"
CMD ["python", "-u", "terminal_app.py"]