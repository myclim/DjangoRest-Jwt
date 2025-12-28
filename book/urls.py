from django.urls import path
from book.views import *

app_name = 'book'

urlpatterns = [
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book_create/', BookCreateView.as_view(), name='book_create'),
    path('book_update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book_remove/<int:pk>/', BookRemoveView.as_view(), name='book_remove')
]
