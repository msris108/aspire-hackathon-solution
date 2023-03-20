# Passwordless Authentication Setup Django

## Environment Setup 
1. git clone aspire-hackathon-solution
2. cd aspire-hackathon-solution
3. python -m venv env
4. pip install -r requirements.txt

## Package Installation
1. use pip install to install packages here, do not use conda
2. pip freeze > ../requirements.txt
3. check dependency list with pip freeze

## Django Setup
1. to start server: python manage.py runserver
2. to make migrations: python manage.py makemigrations
3. to make migrate: python manage.py migrate
4. migration dry run for testing 
5. python manage.py createsuperuser

localhost:8000/admin -> admin panel

## Using environment variables
1. import environ(refer to usage in settings)
2. create .env file in base (/base/.env); refer env.example
3. store key-value pairs, eg. SECRET=abc (**no quotes**)

in python file  
> import environ  
> env = environ.Env()  
> environ.Env.read_env()  
> env('SECRET_VARIABLE')  
 
in /base/.env  
> SECRET_VARIABLE=abcd

NOTE: Backend is optimized for just creating Models and Views. 