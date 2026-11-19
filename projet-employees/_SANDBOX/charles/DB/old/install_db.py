import pymysql
from pymysql.err import MySQLError

# Configuration par défaut pour XAMPP sous Windows
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "",  # Vide par défaut sur XAMPP
    "charset": "utf8mb4",
}

DB_NAME = "db_employees"

SQL_CREATE_DB = f"""
CREATE DATABASE IF NOT EXISTS `{DB_NAME}`
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;
"""

SQL_CREATE_TABLE = f"""
CREATE TABLE IF NOT EXISTS `{DB_NAME}`.`employees` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
"""


def install_database():
    connection = None
    try:
        # 1. Connexion au serveur MariaDB de XAMPP
        connection = pymysql.connect(**DB_CONFIG)
        print("Connexion au serveur MySQL (XAMPP) réussie.")

        with connection.cursor() as cursor:
            # 2. Création conditionnelle de la base de données
            cursor.execute(SQL_CREATE_DB)
            print(f"Base de données '{DB_NAME}' vérifiée/créée.")

            # 3. Création conditionnelle de la table
            cursor.execute(SQL_CREATE_TABLE)
            print("Table 'employees' vérifiée/créée avec succès.")

        connection.commit()

    except MySQLError as e:
        print(f"Erreur MySQL : {e}")

    finally:
        if connection and connection.open:
            connection.close()
            print("Connexion fermée.")


if __name__ == "__main__":
    install_database()