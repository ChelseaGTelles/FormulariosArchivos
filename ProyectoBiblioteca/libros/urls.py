from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  
    path('libros/create/', views.book_create, name='book_create'),  
    path('libros/<int:pk>/', views.book_detail, name='book_detail'),
    path('libros/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('documentos/<int:pk>/delete/', views.document_delete, name='document_delete'),
    path('libros/<int:pk>/delete/', views.book_delete, name='book_delete'),

]
