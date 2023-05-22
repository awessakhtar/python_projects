# Application to get headline News

### video Demo: https://www.youtube.com/watch?v=LvLCO-nZYnk

### Introduction
This project is a news application that allows users to log in or register for an account. After successful login or registration, users can view the top headlines from three popular news channels in Pakistan: Geo News, Samaa English, and The Express Tribune.

### Project Explanation
The application is built using the following technologies:
Flask: A microframework for Python
sqlite3: A lightweight relational database management system
BeautifulSoup: A Python library for web scraping
requests: A Python library for making HTTP requests

The application is structured as follows:
The app.py file contains the main Flask application.
The templates directory contains the HTML templates for the application.
user.db store user data (email and password) for log in purposes.
Bootsrap styling is also incorporated in this project.

The application works as follows:
When a user visits the application, they are presented with a login or register page.

If the user is already logged in, they are taken to the main page, which displays the top headlines from the three news channels.
If the user is not logged in, they can log in or register for an account.
Once the user is logged in, they can view the top headlines from the three news channels.