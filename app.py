#import the flask 
from flask import Flask, jsonify, request 
from flask_migrate import Migrate
from models import db , TokenBlocklist
# authentication from flask jwd 
from flask_jwt_extended import JWTManager
from datetime import datetime
from datetime import timedelta
from flask_mail import Mail,Message




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

#JWT_ 
# Callback function to check if a JWT exists in the database blocklist
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

    return token is not None



# Mail Credentials 
# SMTP credentials
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'sherlyne.ochieng@student.moringaschool.com'
app.config['MAIL_PASSWORD'] = 'slim hbpc dwit bsli'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

#initialize 
mail = Mail(app)

#create an instance of Message 
@app.route('/send_email')
def email():
        msg = Message(
        subject = "First Test Mail Lol, Reply if you receive it lol!",
        sender = "sherlyne.ochieng@student.moringaschool.com",
        #Who you are sending to 
        recipients= ["sherlynea8622@gmail.com","david.kakhayanga@student.moringaschool.com" ],
        #What the message body will send
        body = "Hello,this is the first Flask email from the flask app. GROUP6")
        mail.send(msg)
        return "Message sent Successfully"

if __name__ == '__main__':
    app.run(debug=True)
    
    










