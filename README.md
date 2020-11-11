1. Create django project
Install python3 and virtualenv
Create virtual environment using the command virtualenv -p python3 and activate
Install django==3.1.2 in virtualenv
Create project called Company using the command django-admin startproject company
Create app inside the project => python manage.py startapp staff

2. Make database changes in models and run the following commands

Python manage.py makemigrations

Python manage.py migrate

python manage.py createsuperuser

Python manage.py runserver

3. The admin page can be accessed by the URL http://localhost:8000/admin
4. Department list page - http://localhost:8000/staff/departments/ (department_list.html)
   Department Detail page - http://localhost:8000/staff/department/<Department id> (department_detail.html)
   Create Employee page - http://localhost:8000/staff/create-employee/ (create_employee.html)
  
5. Html template path - /staff/templates/staff/
