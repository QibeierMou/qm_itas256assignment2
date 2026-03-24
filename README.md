# Pizza Delivery Web App - ITAS 256 Assignment 2

A web-based pizza delivery management system built with Flask (Python).

## About
This app allows staff and customers to manage pizza orders through a simple web interface. It was built as part of the Web Development II course (ITAS 256) at Vancouver Island University.

## Features
- User login and account creation
- Create, view, edit and delete pizza orders
- Orders sorted by date (most recent first)
- Calculates subtotal, 10% delivery charge and total per order
- Data stored in JSON files

## Tech Stack
- Python / Flask
- Flask-WTF (forms and validation)
- Jinja2 (HTML templates)
- JSON (data storage)
- CSS (styling)

## How to Run
1. Install dependencies:
```
   uv add flask flask-wtf flask-sqlalchemy flask-cors
```
2. Run the server:
```
   uv run python app.py
```
3. Open your browser to `http://localhost:8888`

## Default Login
- Email: admin123@pizza.com
- Password: admin123

## Author
Jason - ITAS 256 - 2026