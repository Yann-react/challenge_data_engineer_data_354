import pandas as pd

# Fonction pour transformer les données extraites

def transform(df_station):
    # Sélectionner les colonnes numériques
    column_num = df_station.select_dtypes(include=['float64', 'int64']).columns
    
    # Remplacer les valeurs manquantes par la moyenne de chaque colonne
    df_station = df_station.fillna(value=df_station[column_num].mean())
    
    # Supprimer les doublons
    df_station = df_station.drop_duplicates()
    
    #creation de la colonne days pour stocker le temps en jour de la colonne timestamp
    df_station["timestamp"] = pd.to_datetime(df_station["timestamp"])
    df_station["days"] = pd.to_datetime(df_station['timestamp'].dt.date)
    
    # selection des colonnes pour le calcule de la moyenne journalière de CO et PM2.5
    column_for_avg = df_station[["days", "CO", "PM2.5"]]
    avg_by_day = column_for_avg.groupby("days").agg({"CO": "mean", "PM2.5": "mean"})
    avg_by_day = avg_by_day.reset_index()

    # Renommer la colonne "PM2.5" en "PM2_5" pour la manipulation facile lors de requete sql 
    avg_by_day.rename(columns={"PM2.5": "PM2_5"}, inplace=True)
    return avg_by_day  
