from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request: HttpRequest):
    return HttpResponse("<html><title>To-Do lists</title></html>")

