#import the flask 
from flask import Flask, jsonify, request 
from flask_migrate import Migrate
from models import User,Tag,Todo, db

#create a flask class 
app = Flask(__name__)

# #create a migration. config parameters
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

# #initialize the router 
migrate = Migrate(app,db)
db.init_app(app)

#create a router/ where the user will go, 
# Fetch Users/Get Users 

@app.route('/')
def index():
    return "<h1>To-Do Application</h1> <p> This is an Todo Application that utilizes the Flask Packages</p> "


# @app.route('/user/<name>', method = ["GET", "POST"])
# # def user(name):
# #     return f"<h2>Todos for {name} </h2>"
# # pass 

#Fetch/Get Users 
@app.route('/users')
def get_users():
    return jsonify({["events A", "event B"]})

#Add a Users/ Add you use the method POST 
#1. Receive the data in json: 
#To add ? you have to check if the user first exists, if yes you create an error message that the user exist, if not you add the user 
#2. You initialize: data = request.get_json()
@app.route('/users', methods=["POST"])
def add_users():
    data = request.get_json() # This is an object in json 
    username = data['username']
    email = data['email']
    password = data['password']
    
#3. Check if the users exists
    check_username = User.query.filter_by(username=username).first() # first selects the first username in order. 
    check_email= User.query.filter_by(email=email).first()

#4. create an error message if the username or email exists, if yes: return an error message 200/ is just an indication of the error
    #prints the output 
    print("Username", check_username)
    print("Email", check_email)
    
    if check_username or check_email: 
        return jsonify({"error":"username/email already exist"}),406
    else:  # This is where we now add the new username
        new_user = User(username = username, email = email, password = password )
#5. Next you now update/by calling the db.session.add(new_user) db.session.commit()

        db.session.add(new_user)
        db.session.commit()
        return jsonify({"Success": "Users added successfully"})






#Connect to the POSTMAN
#1. Copy the Url http://127.0.0.1:5000