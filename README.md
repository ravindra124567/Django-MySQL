# Django DateTime Retriever

A simple Django web application that retrieves and displays date and time records from a MySQL database.

## Features
- Single button to fetch date/time records
- Display records in a table
- MySQL database integration

## Technologies Used
* Python 3.x
* Django
* MySQL
* HTML/CSS/JavaScript

## Setup Instructions

1. Clone the repository:
```
git clone https://github.com/ManiBharathy-V/Django-MySQL.git
cd Django-MySQL
```
2. Create virtual environment:
```
python -m venv venv
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
source venv/bin/activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Create .env file with your database credentials:
```
DB_NAME=django_testapp
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY=your-secret-key
DEBUG=True
```
5. Create MySQL database:
```
CREATE DATABASE django_testapp;
```
6. Run migrations:
```
python manage.py makemigrations
python manage.py migrate
```
7. Run the development server:
```
python manage.py runserver
```

