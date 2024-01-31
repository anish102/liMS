from django.db import models

# Create your models here.


class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    MembershipDate = models.DateField()


class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=50)


class BookDetails(models.Model):
    DetailsID = models.AutoField(primary_key=True)
    Book = models.OneToOneField(
        Book, on_delete=models.CASCADE, related_name='details')
    NumberOfPages = models.IntegerField()
    Publisher = models.CharField(max_length=255)
    Language = models.CharField(max_length=50)


class BorrowedBooks(models.Model):
    BorrowID = models.AutoField(primary_key=True)
    User = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='borrowed_books')
    Book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='borrowed_by')
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True, blank=True)
