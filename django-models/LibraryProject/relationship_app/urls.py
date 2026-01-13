from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books


urlpatterns = [
    # FBV
    path('books/', views.list_books, name='list_books'),

    # CBV
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Role-Based
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # Auth
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Book Permissions
    path('book/add/', views.add_book, name='add_book'),
    path('book/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
