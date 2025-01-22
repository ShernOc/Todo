from flask import jsonify,request,Blueprint
from models import db,User
from werkzeug.security import generate_password_hash

from flask_jwt_extended import jwt_required, get_jwt_identity


#create a blueprint variable 
#Blueprint(takes in two parameters, the name of blueprint and , __name__) 
user_bp = Blueprint('user_bp', __name__)

#change all the @app to user_bp

#Fetch/Get Users 
@user_bp.route('/users')
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
            # Allows for when fetching a user You are able to see if they are admin or not. 
            "is_admin":user.is_admin,
            "is_approved":user.is_approved,
            #  Use the list comprehension for fetching purposes:
            # Fetching that  allows you to fetch individually a user with its todo or action  
            # ++ todos = db.relationship("Todo",back_populates="user", lazy =True) 
               "todo":[
                {
                    "id":todos.id,
                    "title":todos.title,
                    "description":todos.description,
    
                } for todos in user.todos
            ] 
        })
    return jsonify(user_list)

#Add a Users/ Add you use the method POST 
#1. Receive the data in json: 
#To add ? you have to check if the user first exists, if yes you create an error message that the user exist, if not you add the user 
#2. You initialize: data = request.get_json()
@user_bp.route('/users', methods=["POST"])
def add_users():
    data = request.get_json() # This is an object in json 
    username = data['username']
    email = data['email']
    password = data['password']
    is_admin = data['is_admin']
    
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
@user_bp.route('/users/<user_id>', methods= ["PATCH"])
def update_username(user_id):
    #check if user exists by query.get( which is a default using the get)
    user = User.query.get(user_id)
    
    # data.get[usernmae, user.username] allows one to be able to update the work one by one 
    
    if user: # if user exist
        #get the data 
        data = request.get_json()
        username = data.get('username', user.username)
        email = data.get('email',user.email  )
        password = data.get('password',user.password)
        
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
user_bp.route('/users/<int:user_id>',methods=['DELETE'])
           
def delete_user(user_id):
    #get the users
    user = User.query.get(user_id)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"Success":"User Deleted Successfully"})

    else:
         return jsonify({"Error": "User does not exist"})
     
