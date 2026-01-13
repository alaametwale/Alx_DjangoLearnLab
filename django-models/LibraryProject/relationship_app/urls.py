from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    admin_view,
    librarian_view,
    member_view,
    CustomLoginView,
    CustomLogoutView,
    register,
    add_book,
    edit_book,
    delete_book
)

urlpatterns = [
    # Function-Based Views
    path('books/', list_books, name='list_books'),

    # Class-Based Views
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Role-Based Views
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

    # Authentication
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),

    # Book Permission Views
    path('book/add/', add_book, name='add_book'),
    path('book/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', delete_book, name='delete_book'),
]
