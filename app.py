#import the flask 
from flask import Flask, jsonify, request 
from flask_migrate import Migrate
from models import User, Todo, Tag, db
# authentication from flask jwd 
from flask_jwt_extended import JWTManager

#authentication expires when a users is logged in.
from datetime import timedelta
#importation for backend. 

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.resolve()))

#create a flask class 
app = Flask(__name__)

# #create a migration. config parameters
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

#initialize the router 
migrate = Migrate(app,db)
db.init_app(app)

#import all the functions in views 
from views import * 

#BLUE PRINT
#register the blueprints 
app.register_blueprint(user_bp)
app.register_blueprint(tag_bp)
app.register_blueprint(todo_bp)
# add register the auth
app.register_blueprint(auth_bp)

#AUTHENTICATION 
# imports/ Configuration
# 1. import the jwt (from flask_jwt_extended import JWTManager) 
# 2. Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "sherlyne_Ochieng"

# 3. Add when the authorization will expire: 
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)

# instance of jwt 
jwt = JWTManager(app) 
#4.  initialize the jwt 
jwt.init_app(app)


#create the router 
@app.route('/')
def index():
    return "<h1>To-Do Application</h1> <p> This is an Todo Application that utilizes the Flask Packages</p> "





