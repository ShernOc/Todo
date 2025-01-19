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


#import all the functions in views 
from views import * 

#register the blueprints 
app.register_blueprint(user_bp)
app.register_blueprint(tag_bp)
app.register_blueprint(todo_bp)



#create the router 
@app.route('/')
def index():
    return "<h1>To-Do Application</h1> <p> This is an Todo Application that utilizes the Flask Packages</p> "





