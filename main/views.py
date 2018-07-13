import random

from django.shortcuts import render

from catalog.data import BOOKS


def index(request):
    books = BOOKS[:]
    random.shuffle(books)
    return render(request, 'main/index.html', {
        'books': books[:3]
    })
