import pymysql as pm
try:
    con =pm.connect(host='localhost', database='Amitadb', user='root',password='root')
    cursor= con.cursor()
    query6="insert into Authors(AuthorID,FirstName,MiddleName,LastName) values(1234,'abc','qwe','xyz')"
    cursor.execute(query6)
    query4="insert into Zip_Codes(zip_Code_ID ,City ,State,Zip_Code) values(2,'asd','err',234)"
    cursor.execute(query4)
    query3="insert into Publishers(Publisher_ID ,Name ,Street_Address , Suite_Number ,Zip_Code_ID ) values(234,'ert',34567,45678)"
    cursor.execute(query3)
    query2 ="insert into Titles(TitleID,Title ,ISBN,Publisher_ID ,Publication_Year)values(456,'gj','fht',568,2018)"
    cursor.execute(query2)
    query1="insert into Books(BookID,AuthorID ,TitleID ) values(23,1,456)"
    cursor.execute(query1)
    query5 ="insert into Authors_Titles(Author_Title_ID ,AuthorID ,TitleID) values(123,435,876)"
    cursor.execute(query5)
    print('Table Created')
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
