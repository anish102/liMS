from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book, BookDetails, BorrowedBooks, User
from .serializers import BookSerializer, BorrowedBooksSerializer, UserSerializer


def homepage(request):  # Function to render homepage
    return render(request, 'home.html')


@api_view(['POST'])
# Function to handle HTTP POST request to create user
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# Function to handle HTTP GET request to show all users
def list_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# Function to handle HTTP GET request to show user via id
def get_user_by_id(request, user_id):
    try:
        user = User.objects.get(UserID=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def add_new_book(request):  # Function to handle HTTP POST request to add book
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_all_books(request):  # Function to handle HTTP GET request to show all books
    borrowed_book_ids = BorrowedBooks.objects.values_list('Book_id', flat=True)
    available_books = Book.objects.exclude(BookID__in=borrowed_book_ids)
    serializer = BookSerializer(available_books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# Function to handle HTTP GET request to show book by id
def get_book_by_id(request, book_id):
    try:
        book = Book.objects.get(BookID=book_id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['PUT'])
# Function to handle HTTP PUT request to update/add the details of the book
def assign_update_book_details(request, book_id):
    try:
        book = Book.objects.get(BookID=book_id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def borrow_book(request):  # Function to handle HTTP POST request to borrow book
    serializer = BorrowedBooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
# Function to handle HTTP PUT request to return burrowed books
def return_book(request, borrow_id):
    try:
        borrowed_book = BorrowedBooks.objects.get(BorrowID=borrow_id)
    except BorrowedBooks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    borrowed_book.ReturnDate = request.data.get('ReturnDate')
    borrowed_book.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
# Function to handle HTTP GET request to show all borrowed books
def list_all_borrowed_books(request):
    borrowed_books = BorrowedBooks.objects.filter(ReturnDate__isnull=True)
    serializer = BorrowedBooksSerializer(borrowed_books, many=True)
    return Response(serializer.data)
