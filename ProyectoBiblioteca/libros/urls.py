from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # ruta principal de la app
    path('', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
]

