import os,csv
import pandas as pd



def checkpath():
    listpath=[]
    cwd = os.getcwd()
    print(cwd)
    cwdstr=str(cwd)
    cwdstr.replace("\\",'\\\\')
    print(cwdstr)
           
    print(listpath)
def checkpassword():
    user_password=input("Enter Password")
    hellofile=open('C:\\Users\\USER\\Desktop\\site\\Python-Projects\\School Admission system\\clssteacherPerf\\class2.csv','a',newline='\n')
    csvframe=csv.writer(hellofile)
    csvframe.writerow(t)
        

def login_page(email):
    print("   ")

checkpath()
 