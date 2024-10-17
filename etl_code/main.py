from etl import extract , transform , load
import logging
from dotenv import load_dotenv 
import os

load_dotenv()
# les id des stations
first_station_id = os.getenv("FIRST_STATION_ID")
second_station_id = os.getenv("SECOND_STATION_ID")

api_url = os.getenv("API_URL")

url_db = os.getenv("MONGODB_URL")

logging.basicConfig(format='%(levelname)s: %(message)s',level=logging.DEBUG)
try:
    # extraction des données pour la première station et la deuxième station respectivement a la postion de leur id
    df_first_station = extract(api_url, first_station_id)
    df_second_station = extract(api_url, second_station_id)

    # # Transformation des données de la première station et de la deuxième station
    transform_first_station = transform(df_first_station)
    transform_second_station = transform(df_second_station)


    # Chargement des données de chaque station dans la base de données MongoDB
    load(transform_first_station, "air_quality", "station_283164601",url_db)
    load(transform_second_station, "air_quality", "station_283181971",url_db)

    logging.info("Extraction , transformation et chargement des données ce sont effectué avec succès")

except Exception as e :
    logging.error(f"le pipeline a echoué avec l'erreur:{e}")



