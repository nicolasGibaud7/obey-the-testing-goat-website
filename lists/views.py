from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request: HttpRequest):
    return render(
        request,
        "home.html",
        {"new_item_text": request.POST.get("item_text", "")},
    )
