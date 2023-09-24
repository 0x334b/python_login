import time
import os
username = "admin" # username change here
password = "admin" # password change here

def login():
  os.system("cls")
  user = input("Username : ")
  passwd = input("Password : ")
  if user == username and passwd == password:
    print("succes login")
  else:
    print("Username Or Password Wrong !")
    time.sleep(2.0)
    login()

login()
  
