import sqlite3
conn =sqlite3.connect('pea.db')
print("Opened database Successfully")

cursor = conn.execute("SELECT id, age, name, address, salary from STAFFS")
for row in cursor:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
