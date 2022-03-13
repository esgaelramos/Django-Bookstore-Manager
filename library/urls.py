from django.urls import path
from library import views
from .views import BooksListView, BookDetailView

app_name='library'

urlpatterns = [
    path('', views.home, name='home'),

    path('literature/', views.literature, name='literature'),

    path('contact/', views.contact, name='contact'),

    path('deleteBook/<code>', views.deleteBook),

    path('api/books/', BooksListView.as_view(), name='books-list'),

    path('api/books/<book_slug>', BookDetailView.as_view()),
]

