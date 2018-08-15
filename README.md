 * Introduction
 * Requirements
 * Installation
 * Configuration
 



INTRODUCTION
------------

    This Project is based on searching the users from github API link and store all seached user in database. 

REQUIREMENTS
------------

    There are three basic fundamenetal requirments-
            a)Django==2.0.7
            b)requests==2.10.0


    
INSTALLATION
------------


          a)django(2.0) (pip install django)
          a)requests(2.0) (pip install requests)



CONFIGURATION
-------------
    Run Follwing Commands:
    -python manage.py makemigrations
    -python manage.py migrate
    -python manage.py createsuperuser 
            you have to enter username,email,password
    -python manage.py runserser 0.0.0.0:8000

    open http://127.0.0.0:8000/