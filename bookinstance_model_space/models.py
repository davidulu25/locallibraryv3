# from django.db import models
# from django.conf import settings # to implement user model objects
# from datetime import date

# from book_model_space.models import Book

# import uuid # to support unique book instances

# class BookInstance(models.Model):
#     """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4,
#                           help_text="Unique ID for this particular book across whole library")
#     book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
#     imprint = models.CharField(max_length=200)
#     due_back = models.DateField(null=True, blank=True)
#     borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

#     LOAN_STATUS = (
#         ('m', 'Maintenance'),
#         ('o', 'On loan'),
#         ('a', 'Available'),
#         ('r', 'Reserved'),
#     )

#     status = models.CharField(
#         max_length=1,
#         choices=LOAN_STATUS,
#         blank=True,
#         default='m',
#         help_text='Book availability',
#     )

#     class Meta:
#         ordering = ['due_back']
#         permissions = (("can_mark_returned", "Set book as returned"),)

#     def __str__(self):
#         """String for representing the Model object."""
#         return f'{self.id} ({self.book.title})'
    
#     @property
#     def is_overdue(self):
#         """Determines if the book is overdue based on due date and current date."""
#         return bool(self.due_back and date.today() > self.due_back)