"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import index_view, guest_book_view, guest_book_create_view, guest_book_update_view, \
    guest_book_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('guest_book/<int:pk>/', guest_book_view, name='guest_book_view'),
    path('guest_books/add/', guest_book_create_view, name='guest_book_create'),
    path('guest_book/<int:pk>/update/', guest_book_update_view, name='guest_book_update'),
    path('guest_book/<int:pk>/delete/', guest_book_delete_view, name='guest_book_delete'),
]
