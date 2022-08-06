from django.shortcuts import render
from flask import request

def home(request):
    return render(request, "index.html")