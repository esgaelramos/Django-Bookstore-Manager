from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author, Editorial
from django.db.models import Q #for consultes

#WE USE APIVIEW
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer


def home(request):
    search = request.GET.get('search') #recuperamos la vista

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

def literature(request):
    return render(request, 'literature.html')

def contact(request):
    return render(request, 'contact.html')

def book_detail(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    return render(request, 'book_detail.html', {'book': book})

class BooksListView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()[0:130]
        serializer = PostSerializer(books, many=True)

        return Response(serializer.data)

class BookDetailView(APIView):
    def get(self, request, book_slug, *args, **kwargs):
        book = get_object_or_404(Book, slug=book_slug)
        serializer = PostSerializer(book)

        return Response(serializer.data)
