from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', login_reader),
    path('login/', login_reader, name='login_reader'),
    path('create-reader/', create_reader, name='create_reader'),
    path('create-book/', create_book, name='create_book'),
    path('get-book/', get_book, name='get_book'),
    path('return-book/', return_book, name='return_book'),
    path('logout/', logout_reader, name='logout_reader'),
    path('catalog/', catalog, name='catalog'),

]
