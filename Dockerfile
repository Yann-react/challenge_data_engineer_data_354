# Utiliser une image Python légère
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers de dépendances
COPY requirements.txt .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie de tout les fichiers de l'application ETL dans le conteneur
COPY etl_code/ .  

# Commande pour exécuter le script principal ETL
CMD ["python", "main.py"]
