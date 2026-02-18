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












# run the application 
app.run(debug=True)