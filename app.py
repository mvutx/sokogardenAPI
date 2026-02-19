# import flask and its component 
from flask import *
# import the pymysql module - it helps create a connection bettween python flask and msql database
import pymysql

# create a flask application and give it a name
app = Flask(__name__)


# BELOW IS A SIGNUP ROUTE
@app.route("/api/signup", methods =["POST"])
def signup():
    if request.method=="POST":
        #extract the different details entered on postman form
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        phone = request.form["phone"]

        #by use of the print function print all the details sent with the upcoming reques
        # print(username, email, password, phone)

        #establish a connection between flask/python and mysql
        connection = pymysql.connect(host="localhost", user="root", password="", database="sokogardenonline")


        #create a cursor to execute the sqlqueries
        cursor = connection.cursor()

        #structure an sql to insert the details received on the form 
        #%s is a placeholder-> it stands in places of actual values i.e we shall replace later on 
        sql ="INSERT INTO users(username,email,phone,password) VALUES(%s,%s,%s,%s)"

        # create a tuple that will hold all the data gotten from the form
        data = (username, email, phone, password)

        # by use of the cursor , execute the sql as you replace the placeholder with actual values
        cursor.execute(sql,data)

        #commit the changes to the database 
        connection.commit()


        return jsonify({"message": "User registered successfully"})
#below is the login/signin route 
@app.route("/api/signin", methods=["POST"])    
def signin():
    if request.method == "POST":
        #extracct the to details entered on the form
        email = request.form["email"]
        password = request.form["password"]

        # print out the details
        #print(email, password)

        #create / establish a connecttion  to the database
        connection = pymysql.connect(host="localhost", user="root", password="", database="sokogardenonline")
        # create a cursor 
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        #structure the sql query that will check hether the passord and email entered are correct
        sql="SELECT * FROM users WHERE email = %s AND password = %s"

        # PUT THE DATA RECEIVED  INTO A TUPLE
        data =(email, password)
        # by use of the cursor execute the sql
        cursor.execute(sql, data)
        #check whether there row returned and store the same varable 
        count = cursor.rowcount
        #print(count)

        # if there are  rows return it mean the password  otherwise it means they are wrong
        if count == 0:
            return jsonify({"message": "login failed"})
        else :
            # there must be a user  we create  variable that will hold the details of the user fetched fromthe database
            user=cursor.fetchone()
            #return the details to the content as ell as a message
            return jsonify({"message" : "user logged in successfully", "user":user})
        




# run the application 
app.run(debug=True)