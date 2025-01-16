#import the flask 
from flask import Flask,jsonify, request 
from flask_migrate import Migrate
from models import User,Tag,Todo,db

#create a flask class 
app = Flask(__name__)

#create a migration. config parameters
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

#initialize the router 
migrate = Migrate(app,db)

#create a router/ where the user will go, 

@app.route('/')
def home():
    return "<h1>Todo Application App</h1>"

@app.route('user/', method = ["GET", "POST"])
def user():
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