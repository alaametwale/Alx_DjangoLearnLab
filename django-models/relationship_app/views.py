from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test, permission_required
from .models import Book, Library

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Role-based access
def is_admin(user): return user.userprofile.role == 'Admin'
def is_librarian(user): return user.userprofile.role == 'Librarian'
def is_member(user): return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request): return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request): return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request): return render(request, 'relationship_app/member_view.html')
