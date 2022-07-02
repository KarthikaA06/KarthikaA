import sqlite06
con=sqlite06.connect('user.db')
con.execute("create table users(DOCTOR_NAME,PATIENT_NAME,ISSUSE);")
def insertData(name,actor,actress,director,year):
    qry=f'insert into users (DOCTOR_NAME,PATIENT_NAME,ISSUSE) values ("{doctor_name}","{patient_name}","{issuse}");'
    con.execute(qry)
    con.commit()
    print("add")

def select(doctor_name):
    qry='select * from users where doctor_name="'+doctor_name+'";'
    result=con.execute(qry)
    print("Treatment \t Doctor_Name \t Patient_Name \t Issuse \t")
    for row in result:
        print("|\t ".join(row))
def display():
    qry='select * from users;'
    result=con.execute(qry)
    print("Treatment \t Doctor_Name \t Patient_Name \t Issuse \t")
    for row in result:
        print("|\t ".join(row))

print("1.Insert Data \n2.search patient \n3.display all")
ch="y"
while(ch.lower()=='y'):
    c=int(input())
    if(c==1):
        print("add record")
        doctor_name=input("Enter the name of the doctor:")
        patient_name=input("Enter the name of the paitent:")
        issuse=input("Enter the name of the issue")
        insertData(doctor_name,patient_name,issuse)
    elif (c==2):
        print("select")
        select(input("patient_name:"))
    elif(c==3):
        display()
    else:
        print("Invalied option:" + c)
    ch = input("Do you want to continue[Y/n]: ")
