#  Flask To-Do List Web App

A simple and user-friendly To-Do List web application built with **Flask**, **SQLite**, and **HTML/CSS**.

This app allows users to **register**, **log in**, and manage their daily tasks. It's designed with basic authentication, task CRUD operations, and a clean UI.

---

##  Features

-   User Registration with email, mobile number, DOB, and password
-   Secure Login using hashed passwords (Flask-Bcrypt)
-   Add personal tasks
-   Delete tasks
-   Session-based user authentication
-   SQLite database integration using SQLAlchemy
-   Responsive design using custom CSS


##  Project Structure

Project3-To_Do List/
│
├── app.py # Main Flask application
├── todolist.db # SQLite database (ignored in Git)
├── templates/ # HTML templates (Jinja2)
│ ├── home.html
│ ├── login.html
│ ├── register.html
│ ├── tasks.html
│ └── aboutUs.html
│
├── static/ # Static files (CSS, JS, images)
│ ├── home.css
│ ├── login.css
│ ├── register.css
│ ├── tasks.css
│ └── images/
│ └── HomePageImg.jpg
│
└── .gitignore # Git ignored files (db, venv, etc.)
