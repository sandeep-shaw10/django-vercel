# Django + Vercel + Postgres(Beta)

![Screen shot](./assets/images/screenshot.png)

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

![coverage](https://img.shields.io/badge/version-1.0.0-cyan)

[![coverage](https://img.shields.io/badge/Website-Click%20Here-orange)](https://django-vercel-gules.vercel.app/)

This is a template for a basic portfolio website built with Django, Vercel, and TailwindCSS. The website is hosted on Vercel, using Vercel Storage which provides Postgres for database.

## Requirements
- Python 3.11 or more
- Github Account
- Vercel Account
- Python Requirements

```ssh
asgiref==3.6.0
Django==4.2.1
psycopg2-binary==2.9.6
python-dotenv==1.0.0
sqlparse==0.4.4
tzdata==2023.3
whitenoise==6.4.0
```

## Step-by-Step Guide

### 1. Git Clone via `SSH`, `HTTP` or Download `.zip`

### 2. Add Virtual Environment

Inside Project Directory
```bash
cd django-vercel
```

Create virtual environment 
```bash
python -m venv venv-django
```

Activate Virtual environment
```bash
source venv-django/Scripts/activate
```

### 3. Install Dependency

```python
pip install -r requirements.txt
```

### 4. Add to your Github

Remove git folder
```bash
rm -rf .git
```

Add the files to the new repository and Commit
```python
git add .
git commit -m "Initial commit"
```

Set the remote URL for the new repository
```bash
git remote add origin <new_repository_url>
```

Push the files to the new repository
```bash
git push -u origin master
```

### 5. Link to VERCEL

Link the Github repo to Vercel with this configure project.

Add 5 environment variable
- `ALLOWED_HOSTS`: 127.0.0.1,.vercel.app
- `DEBUG`
- `SECRET_KEY`
- `ADMIN_PATH` (Optional if you don't want your Admin route to be `admin`)
- `POSTGRES_DB_PORT`: 5432

![](./assets/images/v1.png)

After Deployment it's shows Error as it fails to connect to database

![](./assets/images/v2.png)

Connect PostgresSQL from Vercel Storage (Beta feature)
![](./assets/images/v3.png)

After Successfuly connecting the Database, it will add all the environment variable related to Postgres.

![](./assets/images/v4.png)

### 6. Changes from Localhost

Copy all the necessary environment variable to localhost in `.env` to run migration and createsuperuser locally

```env
DEBUG='True'
SECRET_KEY='***'
ALLOWED_HOSTS='127.0.0.1,.vercel.app'
POSTGRES_DATABASE='***'
POSTGRES_USER='***'
POSTGRES_PASSWORD='***'
POSTGRES_HOST='***'
POSTGRES_DB_PORT='5432'
ADMIN_PATH='***'
```

Create superuser
```bash
py manage.py createsuperuser
```

Create Migrations
```bash
py manage.py makemigrations
py manage.py migrate
```

Collect Static
```bash
py manage.py collectstatic
```

### 7. Push to Changes to Github

```bash
git add .
git commit -m "Changes to Static Files"
git push
```

After pushing the repository, vercel will automatically deploy it!

![](./assets/images/v5.png)


### 8. Open your Admin


If ADMIN_PATH is set then path: `app-name.vercel.app/<ADMIN_PATH>`

Otherwise path: `app-name.vercel.app/admin`

![](./assets/images/v6.png)

![coverage](https://img.shields.io/badge/Youtube%20Tutorial-Unavailable-red)]


## Resources and Reference
- [Tailwind Kit](https://www.tailwind-kit.com)
- [Flowbite](https://flowbite.com/)
- [Unsplash](https://unsplash.com/)
- [XSGames: Random User Image Generator](https://xsgames.co/randomusers/)

## Contributing
If you'd like to contribute to this template, please open an issue or submit a pull request.

If you encounter any issues with Python version or operating system compatibility, please feel free to contribute to the repository by submitting an issue or pull request. We welcome all contributions to make this template more accessible to developers on different platforms.

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.