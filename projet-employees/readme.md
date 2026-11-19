
# 🔗 Connexion Django à MySQL (phpMyAdmin)

Ce dépôt montre comment connecter un projet **Django** à une base de données **MySQL** gérée via **phpMyAdmin**, en utilisant un fichier de configuration dédié nommé `connect.py` (à la place du fichier `settings.py` par défaut).

---

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir installé :
* **Python 3.14.6** 
* **Django**
* Un serveur local incluant MySQL et phpMyAdmin **XAMPP**

---
```bash
pip install mysql-connector-python
```

```bash
py -m pip install mysql-connector-python
```
---

<<<<<<< Updated upstream
---
```bash
=======

>>>>>>> Stashed changes
pip install pymysql
py -m pip install pymysql
```
```bash
pip install flask mysql-connector-python
```



### 1. Créer la base de données automatiquement
1. Démarrez les services **Apache** et **MySQL** depuis votre panneau de contrôle (XAMPP/WAMP/etc.).
2. Exécutez le script `install_db.py` fourni dans ce dépôt pour créer automatiquement la base de données dans MySQL via `pymysql` :

```bash
python install_db.py
```

### 2. Configurer le fichier `connect.py`
Ouvrez le fichier `connect.py` (qui remplace `settings.py`) et modifiez la section `DATABASES` avec vos identifiants MySQL :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ma_base_django',     # Nom de la base créée par install_db.py
        'USER': 'root',               # Utilisateur par défaut (souvent 'root')
        'PASSWORD': '',               # Mot de passe (vide par défaut sur XAMPP/WAMP, 'root' sur MAMP)
        'HOST': '127.0.0.1',          # Adresse locale (localhost)
        'PORT': '3306',               # Port MySQL par défaut
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

### 3. Lier `connect.py` au projet (Important)
Comme le fichier de configuration s'appelle `connect.py` et non `settings.py`, vérifiez que la variable d'environnement pointe bien vers ce fichier dans `manage.py`, `wsgi.py` et `asgi.py` :

```python
# Exemple dans manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nom_du_projet.connect')
```

---
## ⚙️ Lancer les migrations et démarrer le serveur

Une fois la configuration terminée, créez les tables par défaut de Django dans phpMyAdmin et lancez le serveur :

```bash
# Générer et appliquer les migrations dans MySQL
python manage.py makemigrations
python manage.py migrate

# Démarrer le serveur de développement
python manage.py runserver
```

Vous pouvez maintenant actualiser **phpMyAdmin** pour vérifier que les tables Django (`auth_user`, `django_migrations`, etc.) ont bien été créées !

---

## 🛠️ Dépannage courant

* **Erreur `No module named 'MySQLdb'`** : Vérifiez que `mysqlclient` est bien installé dans votre environnement virtuel (`pip install mysqlclient`).
* **Erreur d'accès refusé (`Access denied for user`)** : Vérifiez le mot de passe de l'utilisateur `root` dans `connect.py`.

```bash
taskkill /F /IM python.exe
```
pour redemarrer

---
## Here is the SQL INSERT INTO query for 50 employees, restricting the prenom field strictly to Jean, Claire, Lucas, Camille, and Thomas while randomizing the remaining fields:

```SQL
INSERT INTO `employees` (`id`, `nom`, `prenom`, `dextre`, `color`) VALUES
(1, 'Perrin', 'Jean', 'droitier', 'rouge'),
(2, 'David', 'Claire', 'droitier', 'bleu'),
(3, 'Morin', 'Thomas', 'droitier', 'rouge'),
(4, 'Bernard', 'Jean', 'droitier', 'bleu'),
(5, 'Roux', 'Thomas', 'ambidextre', 'bleu'),
(6, 'Chevalier', 'Claire', 'ambidextre', 'rouge'),
(7, 'Roux', 'Camille', 'ambidextre', 'rouge'),
(8, 'Dupont', 'Claire', 'ambidextre', 'rouge'),
(9, 'Dupuis', 'Lucas', 'droitier', 'bleu'),
(10, 'Gautier', 'Lucas', 'droitier', 'bleu'),
(11, 'Rousseau', 'Jean', 'gaucher', 'rouge'),
(12, 'Gauthier', 'Lucas', 'droitier', 'rouge'),
(13, 'Garnier', 'Jean', 'gaucher', 'bleu'),
(14, 'Chevalier', 'Lucas', 'ambidextre', 'rouge'),
(15, 'Francois', 'Claire', 'ambidextre', 'bleu'),
(16, 'Bernard', 'Claire', 'gaucher', 'bleu'),
(17, 'Roux', 'Jean', 'gaucher', 'rouge'),
(18, 'Andre', 'Lucas', 'droitier', 'rouge'),
(19, 'Lambert', 'Claire', 'ambidextre', 'rouge'),
(20, 'Nicolas', 'Jean', 'ambidextre', 'bleu'),
(21, 'Garnier', 'Claire', 'droitier', 'rouge'),
(22, 'Rousseau', 'Lucas', 'ambidextre', 'bleu'),
(23, 'Morin', 'Lucas', 'droitier', 'bleu'),
(24, 'Bernard', 'Lucas', 'gaucher', 'rouge'),
(25, 'Robert', 'Claire', 'ambidextre', 'rouge'),
(26, 'Leroy', 'Camille', 'gaucher', 'rouge'),
(27, 'Laurent', 'Lucas', 'droitier', 'bleu'),
(28, 'Mathieu', 'Thomas', 'ambidextre', 'rouge'),
(29, 'Mathieu', 'Thomas', 'gaucher', 'rouge'),
(30, 'Fontaine', 'Claire', 'droitier', 'rouge'),
(31, 'Richard', 'Jean', 'droitier', 'bleu'),
(32, 'Perrin', 'Claire', 'ambidextre', 'rouge'),
(33, 'Gauthier', 'Jean', 'gaucher', 'rouge'),
(34, 'Gauthier', 'Camille', 'ambidextre', 'rouge'),
(35, 'Chevalier', 'Jean', 'ambidextre', 'bleu'),
(36, 'Morin', 'Thomas', 'gaucher', 'rouge'),
(37, 'Dubois', 'Lucas', 'gaucher', 'bleu'),
(38, 'Andre', 'Jean', 'ambidextre', 'rouge'),
(39, 'Guerin', 'Claire', 'ambidextre', 'bleu'),
(40, 'Perrin', 'Lucas', 'ambidextre', 'bleu'),
(41, 'Laurent', 'Lucas', 'droitier', 'bleu'),
(42, 'Gauthier', 'Lucas', 'gaucher', 'bleu'),
(43, 'Dubois', 'Lucas', 'gaucher', 'bleu'),
(44, 'Petit', 'Claire', 'ambidextre', 'bleu'),
(45, 'Richard', 'Camille', 'droitier', 'bleu'),
(46, 'Moreau', 'Camille', 'ambidextre', 'bleu'),
(47, 'Bertrand', 'Thomas', 'ambidextre', 'rouge'),
(48, 'Leroy', 'Thomas', 'ambidextre', 'bleu'),
(49, 'Henry', 'Lucas', 'gaucher', 'rouge'),
(50, 'Faure', 'Thomas', 'gaucher', 'bleu');
```