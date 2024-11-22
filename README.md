# EmployeeData Project

This is a Django project that allows you to generate, manage, and view employee data. The project uses the Faker library to generate fake data for employees, such as names, email addresses, job titles, salaries, etc. You can filter the data by location, company, and job role. The project provides various views and URLs to display the employee data in different formats and ways.

## Features

- Generate fake employee data using the Faker library
- Filter employee data by location (Hyderabad, Bangalore, Chennai, Pune)
- Display employee details in the admin interface
- Simple CRUD operations for managing employee data
- Data displayed via custom views for each location
- Customizable employee details with the option to filter by company

## Technologies Used

- Python 3.x
- Django 3.x
- MySQL Database (or SQLite for local development)
- Faker Library for generating fake data
- HTML, CSS for the frontend

## Setup Instructions

### 1. Clone the Repository

To get started, clone this repository to your local machine:


git clone https://github.com/Archanapola/EmployeeData.git
cd EmployeeData

2. Create a Virtual Environment
It's recommended to use a virtual environment to avoid conflicts with other Python packages:

python3 -m venv myenv
source myenv/bin/activate  # On Windows use 'myenv\Scripts\activate'

3. Install Dependencies
Install the required dependencies:

pip install -r requirements.txt
If you haven't already installed Faker, you can manually install it with:

pip install faker

4. Configure the Database
In settings.py, ensure your database is properly configured. The default setup is for MySQL. Here’s an example:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employeedb',
        'USER': 'root',
        'PASSWORD': 'your_password_here',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. Apply Migrations
Run migrations to set up your database schema:

python manage.py makemigrations
python manage.py migrate

6. Create a Superuser
   
Create a superuser to access the Django admin panel:
python manage.py createsuperuser

7. Generate Fake Data

To generate fake employee data, navigate to http://127.0.0.1:8000/data/ to populate your database with 10 random employee records.

8. Running the Development Server
Run the Django development server:


python manage.py runserver
Now, you can visit http://127.0.0.1:8000 in your browser.

Views and URLs

/data/: Generates fake employee data.
/fetching_data/: Displays all employee data.
/hyd_data/: Filters employee data by location (Hyderabad).
/bang_data/: Filters employee data by location (Bangalore).
/chennai_data/: Filters employee data by location (Chennai).
/pune_data/: Filters employee data by location (Pune).

Admin Panel
You can manage the data using Django's built-in admin panel. Go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials you created.

To view and manage employee data:
Register the EmployeeData model in admin.py to access it through the Django admin interface.
