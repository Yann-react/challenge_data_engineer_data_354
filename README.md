# challenge_data_engineer_data_354

## Description
Ce projet implémente un processus ETL pour extraire des données de qualité de l'air depuis l'API d'AirQuino, calculer des moyennes journalières, stocker les résultats dans MongoDB, et visualiser les données sur un dashboard Superset.

## Structure du projet
- ```bash etl/ : les scripts etl
- ```bash dashboard/ : le dashboard superset exporté
  
## Prérequis
- Python 3.x
- MongoDB
- Apache Drill
- Superset
- Docker

## Installation
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/Yann-react/challenge_data_engineer_data_354.git
Après le clonage installation des bibliotèque
   ```bash
   pip install -r requirements.txt
2. Installation de MongoDB :
Vous pouvez le téléchargé et l'installé via le lien suivant :
   ```bash
   https://www.mongodb.com/try/download/compass
3. Installation de Apache Drill :
Vous pouvez le téléchargé en suivant la docs via le lien suivant:
   ```bash
   https://drill.apache.org/docs/installing-drill-on-windows/
Après installation lancement du drill web :
   ```bash
   http://localhost:8047/

4.Installation de Docker :
Vous pouvez le téléchargé et l'installé via le lien suivant 
   ```bash
   https://www.docker.com/
5. Installation de Superset
Vous pouvez le téléchargé en suivant la docs via le lien suivant:
   ```bash
   https://superset.apache.org/docs/installation/docker-compose
NB: Ici nous l'avons installé depuis docker donc c'est la docs pour docker qui a été fournit
Après installation lancement de l'interface Superset
   ```bash
   http://localhost:8088/

## Connexion MongoDB à Apach drill
Etant donnée que les donnée issus de MongoDB sont non relationnel il n'est pas possible de faire de la visualisation de ces donnée depuis Superset de cet fait nous passons par Apach drill qui permet de convertir et stocker les donnée non relationnel en relationnel ainsi nous pourrions faire le dashboard .

Après installation nous connectons MongoDB à Apach drill en suivant la docs suivant :
```bash
   https://drill.apache.org/docs/mongodb-storage-plugin/

## Connexion Apach drill a Superset

Pour la connexion de Apach drill a Superset nous installons pip install sqlalchemy-drill dans le dossier cloner de superset lors de son installation après cela nous nous rendons sur l'interface SuperSet dans la section Data puis create "dataset" 
![cap1](https://github.com/user-attachments/assets/388e8ca1-b81b-4559-b1dc-9b70d3c033db)
nous cliquons choisissons Apache drill et mettons
   ```bash
   drill+sadrill://localhost:8047/dfs?use_ssl=False
puis cliquons sur Tester la connexion et valider ainsi nous sommes connecté a Apach drill

## Importation du dashboard
On ce rend dans la setion dashboard et clique sur bouton puis choisir le fichier compresser dans le repertoire dashboard de notre repot git
![cap5](https://github.com/user-attachments/assets/defe6ca8-5228-425d-8fc1-0be91c637ef3)

## Creation d'un dashboard
Pour la creation d'un dashboard suivre ce docs :
   ```bash
   https://superset.apache.org/docs/using-superset/creating-your-first-dashboard
