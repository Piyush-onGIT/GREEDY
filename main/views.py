from http.client import HTTPResponse
from django.shortcuts import render
from flask import request
import db
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.contrib import messages

def home(request):
    return render(request, "index.html")


def edit(request):
    x = db.rows("users")
    print(x)
    db.addUser("piyush", "xyz", "abcd")
    return render(request, "index.html")

def signup(request):
    d = request.POST
    usnm = d['username']
    mail = d['email']
    passd = d['password']
    repass = d['re-pswd']

    if (passd != repass):
        # unmatched password
        messages.info(request, 2)
        return render(request, "index.html")

    check1 = db.check_username(usnm)
    check2 = db.check_mail(mail)

    if check1:
        # username exists
        messages.info(request, 1)
        return render(request, "index.html")
    
    if check2:
        # email exists
        messages.info(request, 3)
        return render(request, "index.html")

    db.addUser(usnm, mail, passd)
        
    return render(request, "index.html")