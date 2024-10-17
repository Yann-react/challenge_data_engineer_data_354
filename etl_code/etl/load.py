from pymongo import MongoClient
import logging

#fonction de chargement des données
def load(df, db_name, collection_name,url):
    """
    Charge les données d'un DataFrame dans une collection MongoDB.

    Args:
        df (DataFrame): Le DataFrame contenant les données à charger.
        db_name (str): Le nom de la base de données MongoDB.
        collection_name (str): Le nom de la collection MongoDB.
        url (str): L'URL de connexion à MongoDB.

    """

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
