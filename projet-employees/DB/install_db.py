import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "",
    "use_pure": True,       # Évite les crashs de socket C-extension avec MariaDB XAMPP
    "ssl_disabled": True,   # Évite la fermeture brutale du handshake SSL sous Windows
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
    cursor = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        print("Connexion au serveur MySQL réussie.")

        cursor.execute(SQL_CREATE_DB)
        print(f"Base de données '{DB_NAME}' prête.")

        cursor.execute(SQL_CREATE_TABLE)
        print("Table 'employees' créée avec succès.")

        connection.commit()

    except Error as e:
        print(f"Erreur MySQL : {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("Connexion fermée.")


if __name__ == "__main__":
    install_database()