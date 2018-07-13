from django.http import Http404
from django.shortcuts import render
from catalog.data import BOOKS

def detail(request, id):
    books = list(filter(lambda b: b['id'] == id, BOOKS))
    if len(books) == 0:
        raise Http404
    return render(request, 'catalog/detail.html', {
        'book': books[0]
    })
