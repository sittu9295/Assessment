# Assessment Tools Project

## Overview
A Django-based web application for creating and managing assessments for teachers and students.

## Features
- Assessment Dashboard
- Assessment Creation Page
- Question Bank Management
- Student Assessment Page
- Feedback and Analytics

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sittu9295/assessment_tool.git
    cd assessment_tool
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Apply migrations and run the server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

## Deployment

The project is hosted on Vercel. To deploy your changes:
```bash
vercel

