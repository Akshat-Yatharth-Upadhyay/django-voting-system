# Pollster - Django Voting System

A simple voting/polling web application built with Python and Django for the Fundamentals of Data Science course.

## Project overview

Pollster allows users to view multiple-choice questions, submit a vote, and immediately see the voting results. An administrator can add and manage questions and choices through Django Admin.

## Technology stack
- Python
- Django
- SQLite
- HTML5
- CSS3

## Main features
- View available polls
- Vote on a multiple-choice question
- Prevent invalid choice submissions
- Display total votes and percentages
- Django Admin for managing questions and choices
- Sample data command for quick demonstration

## How to run

### 1. Create and activate a virtual environment

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create database tables
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Add demonstration data
```bash
python manage.py seed_data
```

### 5. Start the server
```bash
python manage.py runserver
```

Open: http://127.0.0.1:8000/

## Admin panel

Create an admin account:
```bash
python manage.py createsuperuser
```

Then open http://127.0.0.1:8000/admin/

## Project structure

```text
pollster_django/
├── manage.py
├── requirements.txt
├── README.md
├── pollster/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── polls/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── management/commands/seed_data.py
├── templates/
│   ├── base.html
│   └── polls/
│       ├── index.html
│       ├── detail.html
│       └── results.html
└── static/css/style.css
```

## Academic note

This project is based on the Voting System / Pollster project listed in the GeeksforGeeks Django project collection. The implementation and interface in this repository are independently organized for academic demonstration.
