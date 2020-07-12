# DjangoRestApi
Django REST APIs with CRUD Functionality.



## How to run :

* *python3 manage.py makemigrations*
* *python3 manage.py migrate*
* *python3 manage.py runserver*

## URLs for CRUD Functionality:

* Shows the record 
  * http://127.0.0.1:8000/show
* To ADD the record
  * http://127.0.0.1:8000/emp
* To EDIT the record(this option is available with the saved record)
  * http://127.0.0.1:8000/edit/<int:id>
* To DELETE the record(this option is available with the saved record)
  * http://127.0.0.1:8000/edit/<int:id>
* To UPDATE the record(Can be accessed through edit option)
  * http://127.0.0.1:8000/update/<int:id>

## URLs for Django REST APIs:

* **TASK 2.1** (*Average Product Rating of Each Product line Branch wise*):
  * http://127.0.0.1:8000/AverageProductRating/
* **Task 2.2  **(*Top 5 highly rated product line city wise*):
  * http://127.0.0.1:8000/**topfive/**
* **Task2.3** (*Total Amount Payment mode wise*):
  * http://127.0.0.1:8000/Totalamount/