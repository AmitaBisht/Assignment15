import pymysql as pm
try:
    con =pm.connect(host='localhost', database='Amita', user='root',password='root')
    cursor= con.cursor()
    query="select * from Authors"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print("Authors_Title_ID:{},AuthorID:{},TitleID:{}".format(row[0],row[1],row[2]))
    query1="update Authors set FirstName='hgk'"
    cursor.execute(query1)
    data1=cursor.fetchall()
    for row in data1:
        print("Author _Title_ID:{},AuthorID:{},TitleId:{}".format(row[0],row[1],row[2]))
    con.commit()

except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE')
'''import MySQLdb
conn = MySQLdb.connect(host= "localhost", user="root", passwd="root",db="insert")
x = conn.cursor()
x.execute("SELECT *  FROM Amita")
x.execute (" INSERT INTO Amita VALUES ('%s','%s') ", (188,90))
row = x.fetchall()
'''
