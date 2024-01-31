from django.urls import path

from . import views

# Urls for different api endpoints
urlpatterns = [
    path('', views.homepage),
    path('api/users/create/', views.create_user, name='create_user'),
    path('api/users/list/', views.list_all_users, name='list_all_users'),
    path('api/users/<int:user_id>/', views.get_user_by_id, name='get_user'),
    path('api/books/add/', views.add_new_book, name='add_book'),
    path('api/books/list/', views.list_all_books, name='list_books'),
    path('api/books/<int:book_id>/', views.get_book_by_id, name='get_book'),
    path('api/books/<int:book_id>/details/',views.assign_update_book_details, name='details'),
    path('api/borrow/', views.borrow_book, name='borrow_book'),
    path('api/return/<int:borrow_id>/', views.return_book, name='return_book'),
    path('api/borrowed-books/', views.list_all_borrowed_books,name='list_borrowed_books'),
]
