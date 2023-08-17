import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from django.contrib import messages

from catalog.models import Reader

from catalog.forms import ReaderRegisterForm

from catalog.models import Book

from catalog.models import HistoryBook




def home(request):
    current_reader_pk = request.session['current_reader']
    print(current_reader_pk)
    reader = Reader.objects.get(pk=current_reader_pk)
    books = Book.objects.all()
    history_books = HistoryBook.objects.all().order_by('-pk')
    books_current_user = HistoryBook.objects.filter(reader=reader,datetime_return=None)
    context = {
        'reader': reader,
        'books': books,
        'history_books': history_books,
        'books_current_user': books_current_user,
    }
    return render(request, 'catalog/home.html', context)

def create_reader(request):
    if request.method == 'POST':
        form = ReaderRegisterForm(request.POST)
        if form.is_valid():
            reader_instance = form.save()
            request.session['current_reader'] = reader_instance.pk
            return redirect('home')
    return redirect('login_reader')

def get_book(request):
    if request.method == 'GET':
        reader = Reader.objects.get(pk=request.session['current_reader'])
        book = Book.objects.get(pk=request.GET.get('book_pk'))
        book.in_stock = False
        book.save()
        history_book = HistoryBook.objects.create(
            book=book,
            reader=reader,
        )
        return redirect('home')

def return_book(request):
    if request.method == 'GET':
        history_book = HistoryBook.objects.get(pk=request.GET.get('history_book_pk'))
        history_book.book.in_stock = True
        history_book.book.save()
        history_book.datetime_return = datetime.datetime.now()
        history_book.save()
        return redirect('home')

def login_reader(request):
    if request.method == 'POST':
        request.session['current_reader'] = request.POST.get('reader_pk')
        return redirect('home')
    else:
        form = ReaderRegisterForm()

    readers = Reader.objects.all()

    context = {
        'readers': readers,
        'form': form,
    }
    return render(request, 'registration/login.html', context=context)


def logout_reader(request):
    if 'current_reader' in request.session:
        del request.session['current_reader']
    return redirect('login_reader')
