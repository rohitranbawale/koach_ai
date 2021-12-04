import mysql.connector
from flask import Flask, request, jsonify
import json

app = Flask(__name__)


def getMQLDB():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="koach"
    )


    return mydb

def GetData():

    mydb = getMQLDB()

    mycursor = mydb.cursor()


    mycursor.execute("SELECT * FROM employee;")

    myresult = mycursor.fetchall()

    return myresult

def GetSingleUserDetails(email):

    mydb = getMQLDB()

    mycursor = mydb.cursor()

    query = 'SELECT * FROM employee WHERE email="'+email+'";'
    # query2 =
    print("query", query)
    mycursor.execute('INSERT INTO employee (email, password, mobile) VALUES ("bhavesh@gmail.com", "12345" ,"9842638099")')
    # mycursor.execute( val)    
    mydb.commit()
    print(mycursor.rowcount, "Data Inserted.")
    myresult = mycursor.fetchall()

    return myresult


 
@app.route('/getalldata')
def hello_world():

    employees = GetData()

    return json.dumps(employees)

@app.route('/postLogin', methods = ['POST'])
def PostLogin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        mobile = request.form.get('mobile')
        
        userDetails = GetSingleUserDetails(email)

        if len(userDetails) > 0 and userDetails[0][0] == email and userDetails[0][1] == password and mobile == [0][2]:
            return "Login Success"

    return "Login Failure"
 
if __name__ == '__main__':
   # app.run()
 GetSingleUserDetails("9689225354")