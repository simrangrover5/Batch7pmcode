import sqlite3 as sql

db = sql.connect("student.db")
c = db.cursor()
cmd = 'select * from employee'
#cmd = 'select * from employee where eid={}'.format(2)
c.execute(cmd)
data = c.fetchall()
#print(data)
for var in data:
    print("Eid : ",var[0])
    print("Name : ",var[1])
    print("Address : ",var[2])
    print("Ph no : ",var[3])
