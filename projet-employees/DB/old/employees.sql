import pymysql
from pymysql.err import MySQLError

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "",  # Vide par défaut sur XAMPP
    "charset": "utf8mb4",
}

DB_NAME = "db_employees"

SQL_COMMANDS = [
    'SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";',
    'SET time_zone = "+00:00";',
    f"DROP DATABASE IF EXISTS `{DB_NAME}`;",
    f"CREATE DATABASE `{DB_NAME}` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;",
    f"USE `{DB_NAME}`;",
    """
    CREATE TABLE `employees` (
      `id` int(11) NOT NULL,
      `nom` varchar(255) NOT NULL,
      `prenom` varchar(255) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
    """,
]


def reset_database():
    connection = None
    try:
        connection = pymysql.connect(**DB_CONFIG)
        print("Connexion au serveur MariaDB (XAMPP) réussie.")

        with connection.cursor() as cursor:
            for sql in SQL_COMMANDS:
                cursor.execute(sql)

        connection.commit()
        print(f"Base '{DB_NAME}' réinitialisée (supprimée puis recréée) avec succès.")

    except MySQLError as e:
        print(f"Erreur MySQL : {e}")

    finally:
        if connection and connection.open:
            connection.close()
            print("Connexion fermée.")


if __name__ == "__main__":
    reset_database()