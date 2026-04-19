from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're the main page.")
