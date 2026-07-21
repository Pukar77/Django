step-1 pip install Django 
step-2 django-admin startproject myProject
step-3 python manage.py runserver
step-4 python manage.py startapp blog
step-5 register your app name in the installed app inside settings.py


for database (ORM)

python manage.py makemigrations

This command manages the migrations, it does not create a database, but it creates sql files inside migration folder

python manage.py migrate

Inorder to create superuser
python manage.py createsuperuser