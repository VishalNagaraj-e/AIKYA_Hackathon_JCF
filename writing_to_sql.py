import mysql.connector
cnx = mysql.connector.connect(user='root', password='vibhav123',
                              host='127.0.0.1',
                              database='data')
cursor = cnx.cursor()
file = open('1.txt','r')
string = file.read()
list1 = string.split(',')
query = "INSERT INTO data_table VALUES (?, ?, ?, ?, ?)", (list1[0], list1[1], list1[2],list1[3],list1[4])
cursor.execute(query)
cnx.commit()