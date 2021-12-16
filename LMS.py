import os
class Account:
    def __init__(self,account,number,roll="234"):
        self.account=account
        self.number=number
        self.roll=roll
    def change(self):
        p=input("enter the book code")
        if self.roll==input("enter rollno"):
            f=open("rollno.txt","r")
            data=f.read()
            print(data)
        if self.number==int(input("enter id")):
            f1=open("libsoft.txt","a")
            f1.write(data+""+p+""+input("enter the data"))
            f1.close()
        if input("book return code")==p:
            os.remove("libsoft.txt")
    obj=account(7078,"20BQ1A05N9")
    obj.change()
            
            
            