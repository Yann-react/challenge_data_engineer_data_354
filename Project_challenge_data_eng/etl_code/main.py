from etl import extract , transform , load
# les id des stations
first_station_id = 283164601
second_station_id = 283181971

url = f"https://airqino-api.magentalab.it/v3/getStationHourlyAvg/"


# extraction des données pour la première station et la deuxième station respectivement a la postion de leur id
df_first_station = extract(url, first_station_id)
df_second_station = extract(url, second_station_id)


# Transformation des données de la première station et de la deuxième station
transform_first_station = transform(df_first_station)
transform_second_station = transform(df_second_station)


# Chargement des données de chaque station dans la base de données MongoDB
load(transform_first_station, "air_quality", "station_283164601")
load(transform_second_station, "air_quality", "station_283181971")



