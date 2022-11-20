from email.mime import image
from http.client import HTTPResponse
from django.http import HttpResponse 
from multiprocessing import context
import re
from django.shortcuts import render, redirect
from flask import request
import db
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.contrib import messages

# function to get data from saved cookies
def getContext(cookie):
    names = cookie['names']
    number = cookie['number']
    images = cookie['images']

    # convert names(string) to names(list)
    names = names[1:]
    names = names.rstrip(names[-1])
    names = names.split(', ')

    # convert number(string) to number(list)
    number = number[1:]
    number = number.rstrip(number[-1])
    number = number.split(', ')

    # convert images(string) to images(list)
    images = images[1:]
    images = images.rstrip(images[-1])
    images = images.split(', ')

    for i in range(0, len(names)):
        names[i] = names[i][1:]
        names[i] = names[i].rstrip(names[i][-1])

    for i in range(0, len(number)):
        number[i] = number[i][1:]
        number[i] = number[i].rstrip(number[i][-1])

    for i in range(0, len(images)):
        images[i] = images[i][1:]
        images[i] = images[i].rstrip(images[i][-1])

    # zip all the three lists and return it
    context = {"data": zip(number, names, images)}
    return context

# function to open home page(when logged out)
def home(request):
    cookie = request.COOKIES
    try:
        if cookie["login"] == "1":
            context = getContext(cookie)
            return render(request, "afterLog.html", context)
        else:
            print("redirected")
            return render(request, "index.html")
    except:
        return render(request, "index.html")


# signup function
def signup(request):
    d = request.POST
    print(d)
    name = d['fname'] + " " + d["lname"]
    usnm = d['usnm']
    mail = d['email']
    passd = d['passd']
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

    db.addUser(name, usnm, mail, passd)
    return login(request)


# login function
def login(request):
    cookie = request.COOKIES
    # if logged in already, don't read all the data again from db
    try:
        if (cookie['login'] == '1'):
            context = getContext(cookie)
            return render(request, "afterLog.html", context)
    except:
        data = request.POST
        usnm = data['usnm']
        passd = data['passd']

        check = db.check_username(usnm)

        if check:
            if check == passd:
                # logged in
                # messages.info(request, 4)
                
                enrolled = db.getEnCourses(usnm)
                name = []
                image = []
                number = []

                for i in enrolled:
                    details = db.getDetails(i)
                    number.append(str(i))
                    name.append(details[0])
                    image.append(details[1])

                final = zip(number, name, image)
                context = {"data": final}
                response = render(request, "afterLog.html", context)

                # cookies
                response.set_cookie('login', '1')
                response.set_cookie("username", usnm)
                response.set_cookie("names", name)
                response.set_cookie("images", image)
                response.set_cookie("number", number)


                return response
            else:
                # wrong password
                messages.info(request, 5)
                return render(request, "login.html")
        else:
            # no account
            messages.info(request, 6)
            return render(request, "login.html")

        return render(request, "index.html")


# Function to enroll in a course
def enroll(request, course_id):
    cook = request.COOKIES
    course = str(course_id)
    usnm = cook["username"]

    pwd = db.check_username(usnm)
    if pwd:
        db.enroll(course, usnm)
        enrolled = db.getEnCourses(usnm)
        name = []
        image = []
        number = []

        for i in enrolled:
            details = db.getDetails(i)
            number.append(str(i))
            name.append(details[0])
            image.append(details[1])

        final = zip(number, name, image)
        context = {"data": final}
        response = redirect("/")

        # update cookies after getting enrolled
        response.set_cookie("names", name)
        response.set_cookie("images", image)
        response.set_cookie("number", number)

        return response

    return login(request)

# function to open lectures page for each course using course_id
def course(request, course_id):
    cookie = request.COOKIES
    try:
        if (cookie["login"] == "1"):
            course = "course" + str(course_id)
            lecs = db.getLectures(course)
            name = db.getDetails(course_id)[0]

            enrolled = []
            data = getContext(cookie)
            for i, j, k in data["data"]:
                enrolled.append(i)

            if str(course_id) in enrolled:
                context = {"data": lecs, "name": name}
                return render(request, "lectures.html", context)
            else:
                return redirect("/")
        else:
            return redirect("/")
    except:
        return redirect("/")


# logout function
def logout(request):
    cookie = request.COOKIES
    response = render(request, "index.html")
    try:
        # if cookies exist, remove it
        if (cookie["login"] == "1"):
            response.delete_cookie("login", "1")
            return response
        else:
            return redirect("/")
    except:
        return redirect("/")

# function to open teams page
def teams(request):
    return render(request, "aboutus.html")

# function to open login form
def log(request):
    return render(request, "login.html")

# function to open signup form
def reg(request):
    return render(request, "signup.html")