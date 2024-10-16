from pymongo import MongoClient

# # Fonction pour charger les données transformées dans MongoDB

def load(df, db_name, collection_name):
    # Connexion à MongoDB 
    client = MongoClient('mongodb://localhost:27017/')
    db = client[db_name]  # Accéder à la base de données
    collection = db[collection_name]  # Accéder à la collection

    # Convertir le DataFrame en liste de dictionnaires
    data_dict = df.to_dict("records")

    # Insérer les documents dans la collection MongoDB
    collection.insert_many(data_dict)
    print(f"{len(data_dict)} documents insérés dans {collection_name}")  
