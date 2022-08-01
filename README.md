# [TBSSI ELIT]()

**TBSSI ELIT** est une application web qui permet l'automatisation du processus de gestion d'indicateurs et tableaux de bord pour la société El Djazair Information and Technology  

![alt text](https://www.elit.dz/media/file/119/elit_5bceea7a1e81c7.36345187.png)  ![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVNzdLgyAf7SIN8UcmrVGH_48FezNVdcSjRyuRa1GS7AMT-ckq5AOkoWquxQQ3yI7_fg&usqp=CAU) 


> Caractéristiques

- Creer differents profils d'utilisateurs selon leur role dans l'entreprise
- Gerer les indicateurs
- Gerer les tableaux de bord
- Generer des rapport bilan
- Afficher les differents graphes par mois et par année
- Interface Administration pour les adminisrateurs





## ✨  Comment l'utiliser?
```bash
$ # Get the code
$ git clone https://github.com/saber-07/TBSSI_.git
$ cd django-black-dashboard
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$ 
$ # Install modules
$ # SQLIte version
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

<br />

## ✨  Structure de base du code 

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated 
   |    |-- administration/                # app for administration service
   users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- Django bootstrapper `manage.py` uses `core/settings.py` as the main configuration file
- `core/settings.py` loads the app magic from `.env` file
- Redirect the guest users to Login page
- Unlock the pages served by *app* node for authenticated users

<br />





.



### [ChartJs](https://www.chartjs.org/)
---

Chart.js is a free, open-source JavaScript library for data visualization, which supports eight chart types: bar, line, area, pie, bubble, radar, polar, and scatter.

> Install using pip

```bash
$ pip install django-chartjs
```


### [Guardian](https://django-guardian.readthedocs.io/)

---

django-guardian is an implementation of per object permissions on top of Django's authorization backend


> Install using pip

```bash
$ pip install django-guardian

```

> Start the app 

```bash
$ manage.py runserver
Serving on http://localhost:8000
```

Visit `http://localhost:8000` in your browser. The app should be up & running.





## ✨ Credits &  Liens 



### Django , c'est quoi?

**Django** est un framework Web gratuit et open source basé sur Python, qui suit le modèle architectural modèle-modèle-vue. Il est maintenu par la Django Software Foundation, une organisation indépendante établie en tant qu'association 501 à but non lucratif. L'objectif principal de Django est de faciliter la création de sites Web complexes basés sur des bases de données.

### Un tableau de bord, c'est quoi?

Un tableau de bord est un ensemble de pages faciles à lire et offrant des informations à l'utilisateur en temps réel concernant son activité. Un tableau de bord se compose généralement de représentations graphiques de l'état actuel et des tendances au sein d'une organisation. Avoir un tableau de bord bien conçu vous donnera la possibilité d'agir et de prendre des décisions éclairées sur la base des données fournies par votre entreprise




---
[TBSSI] - Pour **[ELIT](https://www.elit.dz/)**.
