# clever_rest
test task

Steps to install:
0. Read https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
1. Install Postgres
2. Create database with name django_base in Postgres
3. Download project from git
4. Change file settings.py section DATABASES (especially password)
5. Enter Virtual Environment and run "pip install -r requirements.txt"
6. Run "python manage.py makemigrations file_app" and python manage.py migrate
7. Run "python manage.py createsuperuser"
8. Run 'python manage.py runserver' 
9. Go to Web browser and type the url 'http://127.0.0.1:8000/api/images/'
