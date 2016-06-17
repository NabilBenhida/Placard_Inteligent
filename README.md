# Placard intelligent

**Première étape:** Ouvrir le terminal

**Cloner le repo:**

```
$ git clone https://github.com/NabilBenhida/Placard_Inteligent
```

**Se rendre dans le projet:**

```
$ cd Placard_Inteligent
```

**Pour se mettre dans l'environnement du projet**

```
$ source projetenv/bin/activate
```

**Pour lancer le serveur**

```
$ cd projet
$ python manage.py runserver 0.0.0.0:8000
```

OUvrez votre navigateur web
tapez l'adresse suivante:

 http://localhost:8000

Le panel admin est disponible à l'adresse:
pour le developper 
http://localhost:8000/admin

**Pour chaque modification des modèles**

Se rendre dans projet

```
$ cd projet
```
Puis
```
$ python manage.py makemigrations
$ python manage.py migrate
```

Pour rendre effectives les modifications sur la base donnéees (modèles)


# Partie pour Julien

Pour se connecter à la base données, se rendre dans projet

```
$ cd projet
```

Puis se connecter à la base de données

```
$ sqlite3 db.sqlite3
```
tu peut faire les requetes dessus
