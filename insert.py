import sqlite3

conn = sqlite3.connect('pea.db')
print("Opened database successfully")
conn.execute("INSERT INTO STAFFS(ID, NAME, AGE, ADDRESS, SALARY)\
VALUES(1, 'PRESBYTERIAN EMANNUEAL ACADEMY', 7, 'KAYOLE', 15000.00)");

conn.execute("INSERT INTO STAFFS(ID, NAME, AGE, ADDRESS, SALARY)\
VALUES(2, 'PRESBYTERIAN EMANNUEAL ACADEMY', 7, 'KAYOLE', 40000.00)");

conn.execute("INSERT INTO STAFFS(ID, NAME, AGE, ADDRESS, SALARY)\
VALUES(3, 'PRESBYTERIAN EMANNUEAL ACADEMY', 7, 'KAYOLE', 25000.00)");

conn.execute("INSERT INTO STAFFS(ID, NAME, AGE, ADDRESS, SALARY)\
VALUES(4, 'PRESBYTERIAN EMANNUEAL ACADEMY', 7, 'KAYOLE', 15000.00)");

conn.commit()
print("Records Created Successfully")
conn.close()
