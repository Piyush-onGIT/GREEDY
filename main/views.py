from http.client import HTTPResponse
import re
from django.shortcuts import render, redirect
from flask import request
import db
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.contrib import messages

def home(request):
    return render(request, "index.html")


def edit(request):
    x = db.rows("users")
    db.addUser("piyush", "xyz", "abcd")
    return render(request, "index.html")

def signup(request):
    d = request.POST
    print(d)
    usnm = d['usnm']
    mail = d['email']
    passd = d['password']
    repass = d['re-passd']

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

def login(request):
    data = request.POST
    usnm = data['usnm']
    passd = data['passd']

    check = db.check_username(usnm)

    if check:
        if check == passd:
            # logged in
            # messages.info(request, 4)
            return render(request, "afterLog.html")
        else:
            # wrong password
            messages.info(request, 5)
            return render(request, "index.html")
    else:
        # no account
        messages.info(request, 6)
        return render(request, "index.html")

    return render(request, "index.html")

def enroll(request):
    data = request.POST
    course = data["course"]
    usnm = data["usnm"]
    pswd = data["passd"]

    pwd = db.check_username(usnm)
    if pwd:
        if (pwd == pswd):
            db.enroll(course, usnm)

    response = redirect('/')
    return response