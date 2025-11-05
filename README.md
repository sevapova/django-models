# django-models

# qadamlar

1. project ni yaratdik: `django-admin startproject core .`
2. app ni yaratdik: `django-admin startapp app`
3. add ni settings ga qoshdik : core/settings.py -> 'INSTALLED_APPS += ['app.apps.AppConfig']`
4. postgresql ni sozladik:
    1. .env ga DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME larni yozdik
    3. core/settings.py 
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv('DB_NAME'),
                'HOST': os.getenv('DB_HOST'),
                'PORT': os.getenv('DB_PORT'),
                'USER': os.getenv('DB_USER'),
                'PASSWORD': os.getenv('DB_PASS'),
            }
        }
        ```
    4. psql postgres shell ga kirib db yaratib oldik
5. app/models.py da model class yaratdik
6. sql structure ga ogirdik modellarni: `python manage.py makemigrations`
7. sql strukturadagi kodlarni postgresql da run qildik: `python manage.py migrate`
8. runserver: `python manage.py runserver`
9. models larni admin panelga qoshidik `app/admin.py`:
    ```python
    from .models import Task
    admin.site.register(Task)
    ```
