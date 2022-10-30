from dataclasses import dataclass
from pickletools import read_uint1
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("dsa.json", scope)
opener = gspread.authorize(creds)
sheet = opener.open("DSA-BOOTCAMP")


def rows(work):
    wks = sheet.worksheet(work)
    return len(wks.get_all_records())

def allRec(work):
    wks = sheet.worksheet(work)
    return wks.get_all_records()

def addUser(name, email, pswd):
    wks = sheet.worksheet("users")
    n = rows("users")
    n += 2
    dt = datetime.now()
    dt.strftime("%d-%m-%Y %H:%M:%S")
    
    wks.update_cell(n, 1, name)
    wks.update_cell(n, 2, email)
    wks.update_cell(n, 3, pswd)
    wks.update_cell(n, 4, str(dt))

def check_username(username):
    wks = sheet.worksheet("users")
    data = wks.get_all_records()

    for i in data:
        if i['username'] == username:
            return str(i['password'])
    return False

def check_mail(mail):
    wks = sheet.worksheet("users")
    data = wks.get_all_records()

    for i in data:
        if i['email'] == mail:
            return True
    return False

    print(data)

def enroll(course, usnm):
    wks = sheet.worksheet("enrolled")
    n = rows("enrolled")
    data = list(wks.get_all_values())
    count = 1
    data.pop(0)

    for i in data:
        if i[int(course) - 1] != '':
            count += 1

    wks.update_cell(count + 1, course, usnm)

def getEnCourses(username):
    wks = sheet.worksheet("enrolled")
    data = list(wks.get_all_values())
    all = []

    for i in data:
        if username in i:
            col = 0
            for j in i:
                col += 1
                if j == username:
                    all.append(col)
    return all

def getDetails(course):
    wks = sheet.worksheet("courses")
    data = list(wks.get_all_values())

    details = []
    for i in data:
        if i[0] == str(course):
            details.append(i[1])
            details.append(i[2])

    return details

def getLectures(course):
    wks = sheet.worksheet(course)
    data = list(wks.get_all_values())
    data.pop(0)

    links = []
    for i in data:
        lst = []
        lst.append(i[0])
        lst.append(i[1])

        links.append(lst)

    return links