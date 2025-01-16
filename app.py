#import the flask 
from flask import Flask, jsonify, request 
from flask_migrate import Migrate
from models import User,Tag,Todo,db

#create a flask class 
app = Flask(__name__)

# #create a migration. config parameters
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

# #initialize the router 
# migrate = Migrate(app,db)

# #create a router/ where the user will go, 

@app.route('/')
def index():
    return "<h1>To-Do Application</h1> <p> This is an Todo Application that utilizes the Flask Packages</p> "

@app.route('user/<name>', method = ["GET", "POST"])
def user(name):
    return f"<h2>Todos for {name} </h2>"
pass 


@app.route('tag/')
def tag():
    pass


@app.route('todo/')
def todo():
    pass 
    




#Run the application: 
if __name__ == '__main__':
    app.run(port=5555, debug=True)