from .models import Author, Book, Library, Librarian

# استعلام جميع الكتب لمؤلف محدد
author = Author.objects.first()
books_by_author = Book.objects.filter(author=author)
print("Books by author:", books_by_author)

# استعلام جميع الكتب في مكتبة
library = Library.objects.first()
library_books = library.books.all()
print("Books in library:", library_books)

# استعلام أمين المكتبة
librarian = Librarian.objects.get(library=library)
print("Librarian:", librarian)
