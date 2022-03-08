from django.shortcuts import render, redirect
from .models import Book, Author, Editorial
from django.db.models import Q #for consultes

def home(request):
    search = request.GET.get('buscar') #recuperamos la vista

    booksList = Book.objects.all()
    authorsList = Author.objects.all()
    editorialsList = Editorial.objects.all()

    if search:
        booksList = Book.objects.filter(
            Q(code__icontains = search) | #Check every model
            Q(book__icontains = search) |
            Q(author__first_name__icontains = search) |
            Q(author__last_name__icontains = search) |
            Q(editorial__editorial__icontains = search)
        ).distinct()


    return render(request, 'home.html', {'books': booksList, 'authors': authorsList, 'editorials': editorialsList})

def deleteBook(request, code):
    book = Book.objects.get(code=code)
    book.delete()
    
    return redirect('/')