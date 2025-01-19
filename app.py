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

#create the router 
@app.route('/')
def index():
    return "<h1>To-Do Application</h1> <p> This is an Todo Application that utilizes the Flask Packages</p> "





