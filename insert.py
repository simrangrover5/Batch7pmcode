import sqlite3 as sql


db = sql.connect("student.db")
c = db.cursor()

#cmd = "create table employee(eid int,name varchar(40),address varchar(50),phno varchar(40))"
#c.execute(cmd)
while True:
    eid = int(input("Enter your eid : "))
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    phno = input("Enter your phno : ")
    cmd = "insert into employee values({},'{}','{}','{}')".format(eid,name,address,phno)
    c.execute(cmd)
    db.commit()
    print("Data inserted")
    ch = input("Do you want to continue or not(yes/no) : ")
    if ch.strip().lower() == "no":
        break
