import os,csv,re




def checkpath():
    cwd = os.getcwd()
    cwdstr=str(cwd)
    a=cwdstr.encode()
    r=re.escape(a)
    b=r.decode()
    return b
    #print(type(b))

def modify_path():
    newpath=input("nameofpath")
    actualpath=checkpath()
    new_modifiedpath=actualpath+newpath
    return new_modifiedpath
def saveentry():
    getpath=(modify_path())
    entry=open(getpath,'a',newline='')
    csvframe=csv.writer(entry)
    #all these are to become new entries in forms to be considered during ui design
    Interns_name=str(input('Interns Name'))
    Campus=str(input('Campus'))
    Phone_number=str(input('Phone Number'))
    From_Start=str(input("Start"))
    To_end=str(input("To "))
    Supervisor=str(input('Supervisor'))
    listclass=[Interns_name,Campus,Phone_number,From_Start,To_end,Supervisor]
    csvframe.writerow(listclass)
    #The print functon is to become a pop up later
    with open getpath 
    print('Entry is recorded')

    
    
           
    
def savepassword():
    user_password=input("Enter Password")
    passwordpath='\\password.csv'
    actualpath=checkpath()
    q=actualpath+passwordpath
    
    hellofile=open(q,'a',newline='\n')
    csvframe=csv.writer(hellofile)
    csvframe.writerow(user_name,q)
        

def login_page(email):
    print("   ")

saveentry()