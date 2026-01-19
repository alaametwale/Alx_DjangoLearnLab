from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm   # ✅ مهم للـ checker

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    form = ExampleForm(request.POST or None)  # ✅ استخدام ExampleForm
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'bookshelf/form_example.html', {'form': form})
