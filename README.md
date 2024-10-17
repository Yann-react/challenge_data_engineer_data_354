# challenge_data_engineer_data_354

## Description
Ce projet implémente un processus ETL pour extraire des données de qualité de l'air depuis l'API d'AirQuino, calculer des moyennes journalières, stocker les résultats dans MongoDB, et visualiser les données sur un dashboard Superset.

## Structure du projet
- `etl/` : les scripts ETL
- `dashboard/` : le dashboard Superset exporté
- `docs/` : la reponse aux questions 


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
   ```

2. Installation de Docker :
   Vous pouvez le télécharger et l'installer via le lien suivant :
   [Télécharger Docker](https://www.docker.com/)

3. Installation de Superset :
   Vous pouvez le télécharger en suivant la documentation via le lien suivant :
   [Documentation d'installation de Superset](https://superset.apache.org/docs/installation/docker-compose)
   **NB** : Ici, nous l'avons installé depuis Docker, donc c'est la documentation pour Docker qui a été fournie. Après installation, lancez l'interface de Superset :
   ```bash
   http://localhost:8088/
   ```
Après leur installation vous entrez dans le dossier du repo cloné a travers votre terminale vous faite la commande suivante :
   ```bash
   docker compose-up --build
   ```
ainsi l'environnement seras mise en place avec le ETL , MongoDB et Apach Drill

## Connexion de MongoDB à Apache Drill
Étant donné que les données issues de MongoDB sont non relationnelles, il n'est pas possible de faire de la visualisation de ces données depuis Superset. De ce fait, nous passons par Apache Drill, qui permet de convertir et de stocker les données non relationnelles en relationnelles, afin de pouvoir créer des dashboards.
Vous vous rendez sur :
   ```bash
   http://localhost:8047/
   ```
Puis, vous vous rendez dans la section "storage" :
![cap_drill](https://github.com/user-attachments/assets/dbfb107d-39dd-4534-b47d-d8e5045275ae)
Vous scrollez vers le bas jusqu'à trouver "mongo" puis vous cliquez sur "enable". Après ça, vous le verrez apparaître dans la liste de gauche, vous cliquez sur "update" :
![cap_drill3](https://github.com/user-attachments/assets/ef516d74-ee7b-4db3-8331-dc98fec8da79)
Vous serez dirigé sur la page de configuration. Au niveau de "connection", mettez :
"mongodb://mongodb:27017/" 
Et vous cliquez sur update.
Pour vérifier que notre DB Mongo a bien été importée, rendez-vous dans la section "query", puis exécutez :
   ```bash
   SHOW DATABASES
   ```
Vous devriez voir apparaître notre table air_quality :
![cap_drilll4](https://github.com/user-attachments/assets/28fdc39c-06cf-4688-ace7-1920b8c7e33c)


## Connexion d'Apache Drill à Superset
Pour la connexion d'Apache Drill à Superset, nous installons sqlalchemy-drill dans le dossier cloné de Superset lors de son installation :.

![cap1](https://github.com/user-attachments/assets/388e8ca1-b81b-4559-b1dc-9b70d3c033db)

Nous choisissons Apache Drill et mettons :
```bash
drill+sadrill://localhost:8047/dfs?use_ssl=False
```
En cas d'échec, remplacez "localhost" par votre adresse IPv4.

Puis, cliquons sur **Tester la connexion** et valider. Ainsi, nous sommes connectés à Apache Drill.

## Importation du dashboard
On se rend dans la section dashboard et clique sur le bouton, puis choisir le fichier compressé dans le répertoire dashboard de notre dépôt Git.

![cap5](https://github.com/user-attachments/assets/defe6ca8-5228-425d-8fc1-0be91c637ef3)

## Création d'un dashboard
Pour la création d'un dashboard, suivez cette documentation :
[Créer votre premier dashboard](https://superset.apache.org/docs/using-superset/creating-your-first-dashboard)

## Notre dashboard
![Capture65](https://github.com/user-attachments/assets/777bdfa4-62af-436b-83b0-1000061a1ed1)

