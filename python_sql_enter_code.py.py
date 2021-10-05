import pymysql

db = pymysql.connect(
	host="localhost",
	user="example",
	passwd="12345",
	database="records"
)
# getting the cursor by cursor() method
mycursor = db.cursor()

insertQuery = "INSERT INTO articles (orderid, customer) VALUES ('345D7','Ahmed');"

mycursor.execute(insertQuery)

print("No of Record Inserted :", mycursor.rowcount)

# we can use the id to refer to that row later.
print("Inserted Id :", mycursor.lastrowid)

# To ensure the Data Insertion, commit database.
db.commit()

# close the Connection
db.close()
