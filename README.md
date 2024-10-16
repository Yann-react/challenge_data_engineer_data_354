# challenge_data_engineer_data_354

## Description
Ce projet implémente un processus ETL pour extraire des données de qualité de l'air depuis l'API d'AirQuino, calculer des moyennes journalières, stocker les résultats dans MongoDB, et visualiser les données sur un dashboard Superset.

## Structure du projet
- `etl/` : les scripts ETL
- `dashboard/` : le dashboard Superset exporté

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
   Après le clonage, installez les bibliothèques :
   ```bash
   pip install -r requirements.txt
   ```

2. Installation de MongoDB :
   Vous pouvez le télécharger et l'installer via le lien suivant :
   [Télécharger MongoDB](https://www.mongodb.com/try/download/compass)

3. Installation de Apache Drill :
   Vous pouvez le télécharger en suivant la documentation via le lien suivant :
   [Documentation d'installation d'Apache Drill](https://drill.apache.org/docs/installing-drill-on-windows/)
   Après installation, lancez l'interface web de Drill :
   ```bash
   http://localhost:8047/
   ```

4. Installation de Docker :
   Vous pouvez le télécharger et l'installer via le lien suivant :
   [Télécharger Docker](https://www.docker.com/)

5. Installation de Superset :
   Vous pouvez le télécharger en suivant la documentation via le lien suivant :
   [Documentation d'installation de Superset](https://superset.apache.org/docs/installation/docker-compose)
   **NB** : Ici, nous l'avons installé depuis Docker, donc c'est la documentation pour Docker qui a été fournie. Après installation, lancez l'interface de Superset :
   ```bash
   http://localhost:8088/
   ```

## Connexion de MongoDB à Apache Drill
Étant donné que les données issues de MongoDB sont non relationnelles, il n'est pas possible de faire de la visualisation de ces données depuis Superset. De ce fait, nous passons par Apache Drill, qui permet de convertir et de stocker les données non relationnelles en relationnelles, afin de pouvoir créer des dashboards.

Après l'installation, nous connectons MongoDB à Apache Drill en suivant la documentation suivante :
[Documentation sur le plugin de stockage MongoDB](https://drill.apache.org/docs/mongodb-storage-plugin/)

## Connexion d'Apache Drill à Superset
Pour la connexion d'Apache Drill à Superset, nous installons `pip install sqlalchemy-drill` dans le dossier cloné de Superset lors de son installation. Ensuite, nous nous rendons sur l'interface de Superset, dans la section Data, puis nous créons un "dataset".

![cap1](https://github.com/user-attachments/assets/388e8ca1-b81b-4559-b1dc-9b70d3c033db)

Nous choisissons Apache Drill et mettons :
```bash
drill+sadrill://localhost:8047/dfs?use_ssl=False
```
Puis, cliquons sur **Tester la connexion** et valider. Ainsi, nous sommes connectés à Apache Drill.

## Importation du dashboard
On se rend dans la section dashboard et clique sur le bouton, puis choisir le fichier compressé dans le répertoire dashboard de notre dépôt Git.

![cap5](https://github.com/user-attachments/assets/defe6ca8-5228-425d-8fc1-0be91c637ef3)

## Création d'un dashboard
Pour la création d'un dashboard, suivez cette documentation :
[Créer votre premier dashboard](https://superset.apache.org/docs/using-superset/creating-your-first-dashboard)
