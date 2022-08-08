from dataclasses import dataclass
from pickletools import read_uint1
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# LF

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