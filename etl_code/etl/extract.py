import pandas as pd
import requests

# fonction d'extraction des données de l'API pour les stations 
def extract(url, station_id):
    """
    Extrait les données de l'API pour une station spécifique.

    Args:
        url (str): L'URL de base de l'API.
        station_id (str): L'identifiant de la station pour laquelle les données doivent être extraites.

    Returns:
        df: Un DataFrame contenant les données extraites de l'API.
    """
     
    url_station = f"{url}{station_id}"    
    #envoie de requet get a l'API et recuperation en json
    response = requests.get(url_station)  
    data = response.json() 
    
    #conversion de la reponse json en data frame
    df = pd.DataFrame(data["data"])  
    return df 