import mysql.connector
import pymongo
import datetime
import sql_connector
import mongodb_connector
mgoclient = pymongo.MongoClient("mongodb://localhost:27017/")

mgodb = mgoclient["temp4"]
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="banking_db"
)

mycursor = db.cursor()
mycursor.execute("show tables")
tables = mycursor.fetchall()

for table in tables:
    print("Table:"+table[0])
    cursor = db.cursor(dictionary=True)
    sql = "select * from " + table[0]
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(result)
    mgocol = mgodb[table[0]]
    for row in result:
        print("row data is:"+str(row))
        for key in row:
            if (isinstance(row[key], datetime.datetime) or isinstance(row[key], datetime.date)):
                row[key] = row[key].strftime('%Y-%m-%d %H:%M:%S')
            # print(key)
        try:
            mgocol.insert_one(row)
        except:
            print("error insert")

    # migrate(db, mgodb, table[0], 1)

print("Done")
