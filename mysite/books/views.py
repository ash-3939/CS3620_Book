from django.shortcuts import render
from .models import BookData

# Create your views here.


def booklist(request):
    book_object = BookData.objects.all()
    return render(request, 'books/book_list.html', {'book_object': book_object})

