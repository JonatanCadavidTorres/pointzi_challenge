from django.http import request
from django.shortcuts import render
from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "core/home.html")


def users_section(request):
    return render(request, "core/users.html")


def books_section(request):
    return render(request, "core/books.html")


# Create your views here.
