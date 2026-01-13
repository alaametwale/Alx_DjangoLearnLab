from .models import Author, Book, Library, Librarian

# --- الاستعلام عن جميع الكتب لمؤلف محدد ---
author_name = "John Doe"  # ضع اسم المؤلف هنا
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

# --- إدراج كافة الكتب في مكتبة ---
library_name = "Central Library"  # ضع اسم المكتبة هنا
try:
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in library_books:
        print(f"- {book.title} by {book.author.name}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

# --- استرداد أمين المكتبة لمكتبة محددة ---
try:
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian found for {library_name}")
