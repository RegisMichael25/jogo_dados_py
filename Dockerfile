# Dockerfile

# Etapa 1: Use uma versão mais recente e segura do Python
FROM python:3.11-slim-bookworm

# Etapa 2: Crie um usuário não-root para segurança
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Etapa 3: Defina o diretório de trabalho e copie os arquivos
WORKDIR /app
COPY requirements.txt .

# Etapa 4: Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código e mude a propriedade para o novo usuário
COPY . .
RUN chown -R appuser:appuser /app

# Etapa 5: Mude para o usuário não-root
USER appuser

# Etapa 6: Exponha a porta e defina o comando de execução
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]