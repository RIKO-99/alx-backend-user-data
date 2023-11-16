# Flask User Authentication with SQLAlchemy 

A Flask project demonstrating user authentication with SQLAlchemy and bcrypt.

## Overview

This project showcases a simple Flask application with user authentication. Users are stored in an SQLite database using SQLAlchemy, and passwords are hashed using bcrypt for enhanced security.

## Features

- Secure password hashing with bcrypt
- User registration and login routes
- Integration with SQLAlchemy for database management
- Demonstrates how to use Flask flash messages

## Getting Started
### Prerequisites

Ensure you have Python, pip, and a virtual environment tool installed on your system.

### Installation

```bash
# Clone the repository
git clone https://github.com/your_username/flask-user-authentication-sqlalchemy.git

# Change into the project directory
cd flask-user-authentication-sqlalchemy

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Unix or MacOS
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

### Challange Requirments 
Allowed editors: vi, vim, emacs
files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.5)
You should use SQLAlchemy 1.3.x
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
All your functions should be type annotated
The flask app should only interact with Auth and never with DB directly.
Only public methods of Auth and DB should be used outside these classes

##### SQLAlchemy Model Mapping
In this project, the User model is mapped to the database using SQLAlchemy. The User class represents a table in the database, and each instance of the class corresponds to a row in that table.
