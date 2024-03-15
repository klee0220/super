# super project
python3 -m venv venv
source venv/bin/activate
git init
git add .
git commit -m 'first commit'
pip install django
django-admin startproject super_app # создаем проект
python manage.py startapp order_app # создаем приложение
python manage.py runserver # тестим сервер 

# миграции
python manage.py makemigrations 
python manage.py migrate

# Создаем БД PostgreSQL
чтобы создать новую БД в консоли пишем:
createdb super_db
sudo -u postgres psql super_db

удалить БД в консоли пишем:
dropdb super_db

устанавливаем pcycopg2
pip install psycopg2==2.9.9

