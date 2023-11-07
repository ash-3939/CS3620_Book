from django.shortcuts import render
from .models import BookData
from django.core.paginator import Paginator

# Create your views here.


def booklist(request):
    book_object = BookData.objects.all()
    bookname = request.GET.get('bookname')
    if bookname != '' and bookname is not None:
        book_object = book_object.filter(name__icontains=bookname)

    paginator = Paginator(book_object, 10)
    page = request.GET.get('page')
    book_object = paginator.get_page(page)
    return render(request, 'books/book_list.html', {'book_object': book_object})
