# Django CRM

## Overview
Django CRM is a customer relationship management (CRM) system built using Django. It provides basic CRUD (Create, Read, Update, Delete) operations for managing customer data efficiently. This application is designed for small businesses and malls to manage customer interactions and information effectively.

## Features
- Add, view, update, and delete customer records.
- Manage customer interactions and history.
- User authentication and authorization.
- Responsive UI for easy navigation.
- Secure and scalable architecture.

## Technologies Used
- Python
- Django
- MySQL (Database)
- HTML, CSS, JavaScript (Frontend)
- Bootstrap (for UI design)

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Virtualenv (optional but recommended)

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/Monicahs/django-crm.git
   cd django-crm
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the server:
   ```bash
   python manage.py runserver
   ```
7. Access the application at `http://127.0.0.1:8000/`.

## Usage
- Log in with the admin credentials created during `createsuperuser` setup.
- Manage customers through the admin panel or dedicated dashboard.
- Use the CRUD functionalities to add, update, or delete customer details.

## Contribution
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your fork and submit a pull request.





