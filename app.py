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
    #query.all gets all the users. 
    users = User.query.all()
    #Convert users to json 
    #create an empty list that will store the users 
    user_list = []
    
    #create a loop that will loop through users 
    for user in users: 
        #in the append pass it as an json objects
        user_list.append({
            "id": user.id,
            "username":user.username,
            "email":user.email,
            "is_approved":user.is_approved  
        })
    return jsonify(user_list)

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

#UPDATE USER: 
#you can update the name, password,email .. 
@app.route('/users/<user_id>', methods= ["PATCH"])
def update_username(user_id):
    #check if user exists by query.get( which is a default using the get)
    user = User.query.get(user_id)
    
    if user: # if user exist
        #get the data 
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        
        #get username and the id is not equal to the username we are searching. 
        #Check if the username or the id is not equal to the id. 
        check_username = User.query.filter_by(username=username and id!=user.id).first()
        check_email = User.query.filter_by(email = email and id!=user.id).first()
        
        if check_username or check_email:
            return jsonify({"error": "Username/Email already exist"}), 406
        
        #and if not, 
        else: 
            #user is the user that was fetched user = User.query.get(user_id)
            user.username = username
            user.email = email
            user.password = password 
        
        #Just commit no adding. 
            db.session.commit()
            return jsonify({"Success": "Users updated successfully"}), 201
#if the user does not exist? 
    else:
        return jsonify({"error": "User does not exist"}), 406
    
    
#DELETE USER; 
@app.route('/users/<int:user_id>',methods=['DELETE'])
           
def delete_user(user_id):
    #get the users
    user = User.query.get(user_id)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"Success":"User Deleted Successfully"})

    else:
         return jsonify({"Error": "User does not exist"})
     
# =========================TAG=================

#Fetch/Get Tags
@app.route('/tags')
def get_tags():
    #query.all gets all the tags 
    tags = Tag.query.all()
    #created an empty list: 
    tag_list = []

    for tag in tags:
        tag_list.append({
            "id":tag.id,
            "name":tag.name
        })
    return jsonify(tag_list)

#ADD A TAG: 
@app.route('/tags', methods=["POST"])
def add_tag():
    #initialize the data 
    data = request.get_json()
    name = data['name']
    
    # check if the name exist 
    check_name = Tag.query.filter_by(name=name).first()
    
    #print the outcome 
    print("name", check_name)
    
    if check_name:
        return jsonify({"error":"Name does not exist"}) , 406 
    else: 
        #add the tag name 
        new_name = Tag(name=name)
        #call/commit
        db.session.add(new_name)
        db.session.commit()
        return jsonify({"Success": "Name added successfully"})
    
 #UPDATE TAG 
@app.route('/tags/<tag_id>', methods = ['PATCH'])        
def update_tag(tag_id):
    tag = Tag.query.get(tag_id)
    
    #check if tag id exists 
    if tag: 
        data = request.get_json()
        name = data['name']
        
        #check if id in not equal to the name
        check_name =Tag.query.filter_by(name = name and id!=tag_id).first()
        
        if check_name: 
            return jsonify({"Error": "Name already exist"})
    
        else: 
        #we are now going to update the tag 
            tag.name = name 
        #commit it
            db.session.commit()
            return jsonify({"Success": "Name was successfully updated"}) , 201 
    
    else:
        return jsonify({"Error": "Name does not exist"}), 406

#Delete Tag: 
@app.route('/tags/<int:tag_id>', methods = ["DELETE"])
def delete_tag(tag_id):
    #get all the data 
    tag = Tag.query.get(tag_id)
    
    if tag: 
        db.session.delete(tag)
        db.session.commit()
        return jsonify({"Success":"Tag deleted successfully"})
    
    else:
        return jsonify({"Error":"Tag does not exist"})
    
    
#=================TODO==============

    
# def update_tags(name)
#     #check if user exists by query.get( which is a default using the get)
#     tags = Tag.query.get(d)
    
#     if user: # if user exist
#         #get the data 
#         data = request.get_json()
#         username = data['username']
#         email = data['email']
#         password = data['password']
        
#         #get username and the id is not equal to the username we are searching. 
#         #Check if the username or the id is not equal to the id. 
#         check_username = User.query.filter_by(username=username and id!=user.id).first()
#         check_email = User.query.filter_by(email = email and id!=user.id).first()
        
#         if check_username or check_email:
#             return jsonify({"error": "Username/Email already exist"}), 406
        
#         #and if not, 
#         else: 
#             #user is the user that was fetched user = User.query.get(user_id)
#             user.username = username
#             user.email = email
#             user.password = password 
        
#         #Just commit no adding. 
#             db.session.commit()
#             return jsonify({"Success": "Users updated successfully"}), 201
# #if the user does not exist? 
#     else:
#         return jsonify({"error": "User does not exist"}), 406
    
    
# #DELETE USER; 
# @app.route('/users/<int:user_id>',methods=['DELETE'])
           
# def delete_user(user_id):
#     #get the users
#     user = User.query.get(user_id)
    
#     if user:
#         db.session.delete(user)
#         db.session.commit()
#         return jsonify({"Sucess":"User Deleted Successfully"})

#     else:
#          return jsonify({"Error": "User does not exist"})



