import pandas as pd
import requests

# fonction d'extraction des données de l'API pour les stations 

def extract(url, station_id):
    url_station = f"{url}{station_id}"    
    #envoie de requet get a l'API et recuperation en json
    response = requests.get(url_station)  
    data = response.json() 
    
    #conversion de la reponse json en data frame
    df = pd.DataFrame(data["data"])  
    return df 