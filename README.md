- mkdir vercel_postgres
- cd vercel_postgres
- py -m venv venv-django
- source venv-django/Scripts/activate
- pip install Django
- pip freeze > requirements.txt
- django-admin startproject core .
- py manage.py runserver

- django-admin startproject app
- edit: "view", "urls", "core/urls", "core/settings"

- change sqlite3 to postgres
- fetch users: "core/utils/user"
- edit: "view" allUsers

- add vercel.json

- py manage.py makemigrations 
- py manage.py migrate
- py manage.py createsuperuser

Tools
- https://www.tailwind-kit.com
- https://flowbite.com/
- https://unsplash.com/
- https://xsgames.co/randomusers/