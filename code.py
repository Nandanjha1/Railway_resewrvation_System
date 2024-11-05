import mysql.connector   
mycon=mysql.connector.connect(host="localhost",user="root",password="Nandan@123")
cursor=mycon.cursor()
mycon.autocommit=True

s1="create database if not exists railway"
cursor.execute(s1)
s1="use railway"
cursor.execute(s1)

s1="create table if not exists railway(name varchar(100),phno varchar(15) primary key,age int(4),gender varchar(50),from_f varchar(100),to_t varchar(100),date_d varchar(20))"
cursor.execute(s1)

s1="create table if not exists user_accounts(fname varchar(100),lname varchar(100),user_name varchar(100),password varchar(100) primary key,phno varchar(15),gender varchar(50),dob varchar(50),age varchar(4))"
cursor.execute(s1)
def signin():
    a=input("USER NAME:")
    b=input("PASSWORD:")
    s="select user_name from user_accounts where password='{}'".format(b)
    cursor.execute(s)
    data=cursor.fetchone()
    if data[0]==a:
        print("\t\t\t\t________________")
        print("\t\t\t\t\t\tLOGIN SUCESSFULLY ")
        print("\t\t\t\t________________")
        main()
    else:
        print("ACCOUNT DOES NOT EXIST OR WRONG ENTRY")    

def signup():
    f=input("FIRST NAME:")
    l=input("last NAME:")
    a=input("USER NAME")
    b=input("PASSWORD:")
    c=input("RE-ENTER YOUR PASSWORD:")
    ph=input("PHONE NUMBER:")
    print('M=MALE\n','F=FEMALE\n','N=NOT TO MENTION')
    gen=input("ENTER YOUR GENDER:")
    print("ENTER YOUR DATE OF BIRTH:")
    d=input("DD:")
    o=input("MM:")
    p=input("YYYY:")
    dob=d+'/'+ o+'/'+p
    age=input("YOUR AGE:")
    v={'M':'MALE','F':'FEMALE','N':'NOT TO MENTION'}
    if b==c:
        c1="insert into user_accounts values('{}','{}','{}','{}','{}','{}','{}','{}')".format(f,l,a,b,ph,gen,dob,age)
        cursor.execute(c1)
        print("\t\t\t\t________________")
        print("\t\t\t\t\t\tSIGN UP SUCESSFULLY ")
        print("\t\t\t\t________________")
        main()
    else:
        print("BOTH PASSWORD ARE NOT MATCHING")
        
def ticket_booking():
    nm=input("Enter Your Name:") 
    phno=input("Enter Your Phone Number:")
    age=int(input("Enter Your Age:"))
    print("'M=MALE','\t','F=FEMALE','\t','N=NOT TO MENTION'")
    gender=input("Enter your Gender:")
    Gender=gender.upper()
    fr=input("Enter Starting Point:")
    to=input("Enter your Destination:")
    date1=input("Enter date(DD):")
    date2=input("Enter month(MM):")
    date3=input("Enter Year(YYYY):")
    date=date1+"/"+date2+"/"+date3
    a={'M':'MALE','F':'FEMALE','N':'NOT TO MENTION'}
    v=a[Gender]
    s1="insert into railway values('{}','{}','{}','{}','{}','{}','{}')".format(nm,phno,age,v,fr,to,date)
    cursor.execute(s1)
    print("\t\t\t\t________________")
    print("\t\t\t\t\t\tTICKET BOOKED SUCESSFULLY ")
    print("\t\t\t\t________________")
def ticket_checking():
    phno=input("Enter Your Phone Number:")
    try:
        s1=("select * from railway where phno='{}'".format(phno))
        cursor.execute(s1)
        data=cursor.fetchone()
        Data=list(data)
        a=['NAME','PHONE NUMBER','AGE','GENDER','STARTING POINT','DESTINATION','DATE']
        print(a[0],'::::',Data[0])
        print(a[1],'::::',Data[1])
        print(a[2],'::::',Data[2])
        print(a[3],'::::',Data[3])
        print(a[4],'::::',Data[4])
        print(a[5],'::::',Data[5])
        print(a[6],'::::',Data[6])
    except:
        print("TICKET DOES NOT EXISTS")
def ticket_cancelling():
    phno=input("Enter your phone number:")
    s="select phno from railway where phno='{}'".format(phno)
    cursor.execute(s)
    data=cursor.fetchone()
    if data[0]==phno:
        s1="delete from railway where phno=phno"
        cursor.execute(s1)
        print("\t\t\t\t________________")
        print("\t\t\t\t\t\tTICKET CANCEL SUCESSFULLY ")
        print("\t\t\t\t________________")
        main()
    else:  
        print("TICKET DOES NOT EXIST OR WRONG ENTRY")  
    
def display():
    a=input("USER NAME:")
    b=input("PASSWORD:")  
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        c1="select fname,lname from user_accounts where password='{}'".format(b)
        cursor.execute(c1)
        data1=cursor.fetchall()[0]
        data1=list(data1)
        data1=data1[0]+''+data1[1]
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==a:
            x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
            s1="select fname,lname,phno,gender,dob,age from user_accounts where password='{}'".format(b)
            cursor.execute(s1)
            data=cursor.fetchall()[0]
            data=list(data)
            print(x[0],'::::',Data[0])
            print(x[1],'::::',Data[1])
            print(x[2],'::::',Data[2])
            print(x[3],'::::',Data[3])
            print(x[4],'::::',Data[4])
            print(x[5],'::::',Data[5])
        else:
            return False
    except:
        print("ACCOUNT DOES NOT EXIST")
           
    
def main():
    while True:
        print("\t\t\t\t________________")
        print("\t\t\t\t\t\t1.TICKET BOOKING")
        print("\t\t\t\t\t\t2.TICKET CHECKING")
        print("\t\t\t\t\t\t3.TICKET CANCELLING")
        print("\t\t\t\t\t\t4.ACCOUNT DETAILS")
        print("\t\t\t\t\t\t5.LOG OUT")
        print("\t\t\t\t________________")
        ch=int(input("\t\t\tENTER YOUR CHOICE:"))
        if ch==1:
            ticket_booking()
        elif ch==2:
            ticket_checking()
        elif ch==3:
            ticket_cancelling()
        elif ch==4:
            display()
        elif ch==5:
            print("________________________________")
            print("\t\t\t\t\t\tLOG OUT SUCESSFULLY")
            print("________________________________")
            break
        else:
            print("ERROR 404:ERROR PAGE NOT FOUND")
print("_____________________________________")
while True:
    print("\t\t\t\tWELCOME TO ONLINE RAILWAY RESERVATION SYSTEM")
    print("\t\t\t\t________________")
    print("\t\t\t\t\t\t1.SIGN IN")
    print("\t\t\t\t\t\t2.SIGN UP")
    print("\t\t\t\t\t\t3.EXIT")
    print("\t\t\t\t________________")
    print("_____________________________________")
    ch=int(input("\t\t\t\tENTER YOUR CHOICE :"))
    if ch==1:
        signin()
    elif ch==2:
        signup()
    elif ch==3:
        print("\t\t\t\t________________")
        print("\t\t\t\t\t\tEXIT SUCESSFULLY!!")
        print("\t\t\t\t________________")
        break
    