The library management system is created to be used solely by the library administrations. I also made the assumption that the library contains only one of the particular book.  
  
***Setup***:  
Generally, it is recommended to do project in the python virtual environment, so did I.  
First, create the python virtual environment through the command: *python -m venv env_name*  
The environment can be activated by the command: *source env_name/bin/activate*  
Then install the required tools and packages which I have listed on requirements.txt file which can be directly installed through the command: *pip install -r requirements.txt*  
Then create the django project: *django-admin startproject project_name*  
Then create the django app: *python manage.py startapp app_name*  
Then set up the database to integrate with django.  
Add the installed apps such as django rest framework and the created app as well as database properties on settings.py file.  
Create a serializers.py file to serialize output of the response.  
Add your logics and data schema to views.py and models.py file.  
Create the url to map the api endpoints to the respective view functions.  
Make sure all the api endpoints are working as desired.  
Finally, push the project in remote github repository.  
  
***Api description***:  
Through the api endpoints of library management system, we can create users, add books, as well as keep a record of borrowed and returned books.  
**User endpoints**  
*GET /api/users/list/*  
Description: Endpoint to retrieve a list of all users in the system.  
  
*POST /api/users/create/*  
Description: Endpoint to create a new user in the system.  
Parameters:  
name (string): The name of the user.  
email (string): The email of the user.  
membership_date (date): The date the user's membership started.  
  
*GET /api/users/{user_id}/*  
Description: Endpoint to retrieve details of a specific user by user ID.  
Parameters:  
user_id (integer): The ID of the user.  
  
**Book Endpoints**:  
*GET /api/books/list/*  
Description: Endpoint to retrieve a list of all books in the library.  
  
*POST /api/books/add/*  
Description: Endpoint to add a new book to the library.  
Parameters:  
title (string): The title of the book.  
isbn (string): The ISBN of the book.  
published_date (date): The published date of the book.  
genre (string): The genre of the book.  
quantity (integer): The quantity of the book available in the library.  
  
*GET /api/books/{book_id}/*  
Description: Endpoint to retrieve details of a specific book by book ID.  
Parameters:  
book_id (integer): The ID of the book.  
  
*PUT /api/books/{book_id}/details*  
Description: Endpoint to update details of a specific book by book ID.  
Parameters (Optional):  
title (string): The title of the book.  
isbn (string): The ISBN of the book.  
published_date (date): The published date of the book.  
genre (string): The genre of the book.  
quantity (integer): The quantity of the book available in the library.  
  
**Borrowed Books Endpoints:**  
*GET /api/borrowed-books/*  
Description: Endpoint to retrieve a list of all borrowed books in the library.  
  
*POST /api/borrow/*  
Description: Endpoint to borrow a book from the library.  
Parameters:  
user_id (integer): The ID of the user borrowing the book.  
book_id (integer): The ID of the book being borrowed.  
borrow_date (date): The date the book is borrowed.  
return_date (date): The expected return date of the book.  
  
*PUT /api/return/{borrowed_book_id}/*  
Description: Endpoint to return a borrowed book to the library.  
Parameters:  
borrowed_book_id (integer): The ID of the borrowed book being returned.  
  
***HTTP status codes used by liMS api***:  
200 OK: Successful  
201 OK: Created  
400 Bad Request: Bad input parameter  
404 Not Found: Resource not found  
