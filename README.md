# Employee Analytics & Management System

A full-stack web application built using **Django** that allows organizations to manage employee records and visualize analytics through an interactive dashboard.

## Features

- Employee CRUD operations (Create, Read, Update, Delete)
- Cloud-based image upload using **Cloudinary**
- Interactive analytics dashboard using **Chart.js**
- Employee statistics cards
- Responsive UI with **Bootstrap**
- Department-based employee analytics
- Secure form handling

## Tech Stack

Backend:
- Python
- Django

Frontend:
- HTML
- Bootstrap
- Chart.js

Data Processing:
- Pandas

Cloud Services:
- Cloudinary (Image Storage)

Database:
- SQLite

## Project Structure

employee-analytics-system
│
├── config
│   ├── config
│   ├── employees
│   └── manage.py
│
├── requirements.txt
├── .gitignore
└── README.md

## Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/employee-analytics-system.git

Navigate into the project:

cd employee-analytics-system

Create virtual environment:

python -m venv venv

Activate environment:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Run server:

python manage.py runserver

Open in browser:

http://127.0.0.1:8000

## Future Improvements

- Role-based authentication
- More analytics visualizations
- Production database integration
