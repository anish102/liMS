from django.urls import path

from . import views

urlpatterns = [
    path('users/create/', views.create_user),
    path('users/list/', views.list_all_users),
    path('users/<int:user_id>/', views.get_user_by_id),
    path('books/add/', views.add_new_book),
    path('books/list/', views.list_all_books),
    path('books/<int:book_id>/', views.get_book_by_id),
    path('books/<int:book_id>/details/', views.assign_update_book_details),
    path('borrow/', views.borrow_book),
    path('return/<int:borrow_id>/', views.return_book),
    path('borrowed-books/', views.list_all_borrowed_books),

]
