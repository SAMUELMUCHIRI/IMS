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

checkpath()
modify_path()