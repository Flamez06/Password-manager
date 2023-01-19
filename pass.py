from cryptography.fernet import Fernet
import os.path
import json

exists1=os.path.exists("mypas.txt")
exists2=os.path.exists("pass.json")
if exists1!=True:
    key=Fernet.generate_key()
    with open("mypas.txt","a") as f:
        f.write(key.decode('utf-8'))
if exists2!=True:
    d={}
    with open("pass.json","a") as f:
        json.dump(d,f)


with open("mypas.txt","r") as f:
   f=Fernet(bytes(f.read(),'utf-8'))

def password(choice):
    with open("pass.json","r")as y:
            x=json.load(y)
    if choice not in ("1","2"):
        print("Invalid. Please try again.")
    elif choice=="1":
        print("Enter what the password is for followed by the password itself with a space in between:")
        a=input().split()
        a[1]=f.encrypt(bytes(a[1],"utf-8"))
        dict={a[0]:a[1].decode('utf-8')}
        x.update(dict)
        with open("pass.json","w")as y:
            json.dump(x,y)
        print("Your password has been saved successfully.")
    else:
        a=input("Enter which password you want to view: ")
        if a not in x.keys():
            print("There is no saved password for your input. Try again or save the password first.")
        else:
            b=f.decrypt(bytes(x[a],'utf-8'))
            print(a,":",b.decode('utf-8'))
    y=input("Do you want to continue? If yes press y else program will auto end.\n")
    if y.lower()!="y":exit()

while True:
    choice=input("What do you want to do? \nStore a new password (1)\nView existing passwords (2)\nExit (3)\n")
    if choice=="3":
        break
    password(choice)
