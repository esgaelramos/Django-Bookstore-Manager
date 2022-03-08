from django.urls import path
from library import views


# from library import views

app_name='library'

urlpatterns = [
    path('', views.home, name='home'),

    path('deleteBook/<code>', views.deleteBook),
    # path('hello-world', views.HelloWorld, name='hello-world'),
]
