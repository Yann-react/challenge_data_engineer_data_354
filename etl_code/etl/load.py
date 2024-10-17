from pymongo import MongoClient
import logging

def load(df, db_name, collection_name,url):
    # Connexion à MongoDB
    client = MongoClient(url)
    logging.info(f"Connexion a MongoDB sur {url}")
    try:
        db = client[db_name]  # Accéder à la base de données
        collection = db[collection_name]  # Accéder à la collection

        # Convertir le DataFrame en liste de dictionnaires
        data_dict = df.to_dict("records")

        # Insérer les documents dans la collection MongoDB
        collection.insert_many(data_dict)
        logging.info(f"{len(data_dict)} documents insérés dans {collection_name}")
    except Exception as e:
        logging.error(f"echec de la connexion MongoDB: {e}")
