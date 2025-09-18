# University Management System

A Django-based university management system for managing students, teachers, courses, departments, and marks.

## Quick Start Commands

### 1. Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 2. Run Database Migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 3. Create Admin User
```bash
python3 manage.py createsuperuser --username admin --email admin@example.com --noinput
python3 manage.py shell -c "from django.contrib.auth.models import User; u = User.objects.get(username='admin'); u.set_password('admin123'); u.save(); print('Password set successfully')"
```

### 4. Run the Development Server
```bash
python3 manage.py runserver
```

## Access URLs

- **Main Application**: http://127.0.0.1:8000/
- **Admin Interface**: http://127.0.0.1:8000/admin/
  - Username: `admin`
  - Password: `admin123`

## System Requirements

- Python 3.9+
- Django 4.2+
- SQLite3 database
