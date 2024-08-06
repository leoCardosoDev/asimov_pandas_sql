# Use uma imagem base do Python
FROM python:3.12

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Atualize pip e instale dependências
RUN pip install --upgrade pip

# Copie os requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o conteúdo do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Defina o comando padrão para manter o contêiner em execução
CMD ["tail", "-f", "/dev/null"]
