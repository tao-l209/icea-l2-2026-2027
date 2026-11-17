
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

---
```bash
pip install pymysql
py -m pip install pymysql
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