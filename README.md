# Web Application for Activity Management

This README provides an overview of a web application developed using Django for backend management, JavaScript for interactivity, and MySQL for data storage. The application is designed to manage activities for administrators and faculty members, allowing seamless logging and monitoring of activities.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Usage](#usage)
7. [User Roles](#user-roles)
8. [Future Enhancements](#future-enhancements)
9. [License](#license)

## Introduction

This web application enables faculty members to log their activities while providing administrators with the tools to monitor these activities, apply filters, and export data for reporting purposes. It fosters transparency and accountability within the institution.

## Features

### For Admins
- **Monitor Activities**: Access and view all logged activities from faculty members.
- **Filter Data**: Use filters to sort data based on date, activity type, or specific faculty.
- **Export to Excel**: Export filtered data to Excel format for further analysis or reporting.

### For Faculty
- **Add Activities**: Easily log activities, including relevant details such as date, description, and type.
- **View Activity Log**: Access their personal history of logged activities.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Development Tools**: Django REST Framework (for API development)

## Requirements

### Software
- Python 3.x
- Django (version 3.0 or higher)
- MySQL (version 5.7 or higher)
- Node.js (optional, for JavaScript libraries)
- A modern web browser

### Hardware
- Any computer capable of running Django and a MySQL server.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MySQL Database**:
   - Create a new MySQL database and user.
   - Update the `settings.py` file in your Django project with the database connection details:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'yourdbname',
             'USER': 'yourusername',
             'PASSWORD': 'yourpassword',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Application**:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**:
   Open your web browser and navigate to `http://localhost:8000`.

## Usage

1. **Admin Login**:
   - Access the admin dashboard using the superuser credentials created during setup.
   - Monitor activities, apply filters, and export data as needed.

2. **Faculty Login**:
   - Faculty can log in using their credentials to access the faculty dashboard.
   - They can log new activities and view their past entries.

## User Roles

- **Admin**:
  - Full access to view all faculty activities.
  - Capable of filtering and exporting data.
  - Manages overall application settings and user accounts.

- **Faculty**:
  - Can log their own activities.
  - Can view and edit their activity history.
  - Limited access compared to admin roles.

## Future Enhancements

- **User Notifications**: Implement a notification system to alert users of important updates.
- **Advanced Analytics**: Introduce visual analytics to track activity trends over time.
- **Mobile Responsiveness**: Enhance the frontend to ensure usability on mobile devices.
- **Role Management**: Further expand role management to include custom roles or permissions.

## License

This project is open-source and available for modification and use. Please attribute the original source if you adapt this work.
