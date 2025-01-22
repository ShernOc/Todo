from flask_jwt_extended import jwt_required, get_jwt_identity

#FLASK NOTES: 

#Update user 
#Delete User 

# @app.route('/todo')
# #Receive the data in json 
# def add_todo():
#     data = request.get_json()
       
# #Run the application: 
# if __name__ == '__main__':
#     app.run(port=5555, debug=True)
    
# # #To add 
# # user = User()
# # db.session.add(user)
# # db.session.commit()


# # #To update/modify data 
# # user.verified = True
# # db.session.commit()

# # #to delete
# # db.session.delete(user)
# # db.session.commit()


#Add a Users/ Add you use the method POST 
#1. Receive the data in json: 
#To add ? you have to check if the user first exists, if yes you create an error message that the user exist, if not you add the user 
#2. You initialize: data = request.get_json()
    
#3. Check if the users exists by using filter_by or filter(username)

#4. create an error message if the username or email exists, if yes: return an error message 200/ is just an indication of the error
    #prints the output
    
#5. Next you now update/by calling the db.session.add(new_user) db.session.commit()

#6 return jsonify({Successfully})

#Connect to the Postman
#Connect to the POSTMAN
#1. Copy the Url http://127.0.0.1:5000


#   QUESTIONS
#How to update just the name? 
#How to 


#Friday 17th Meeting: 
#FETCHING 
#Fetching One thing alone: 

 #create a relationship with the Todo Table
 # From the modeling 
    #Allows us to create a fetcheing
    # +todos = db.relationship("Todo",back_populates="user", lazy =True)
    
#UPDATING: 
#Wanting to just update one thing: 

#Allowing only one thing to be updated: We use the  data.get() method : In the Update section 
#updating section
# if the user does not pass, or type you add the (user.username # what is going to be fetched if the client does not input. )
# username = data.get('username', user.username)

# is_complete: in models 


#AUTHENTICATION 
#Authentication: verifying users identity 
# Authorization: verification of what a user can user. 

# - Password needs to be hashed in the user.py (from werkzeug.security import generate_password_hash)

#STEPS: 
#1.  install the pip install flask-jwt-extended
#2. Go to the app.py and : 

# imports/ Configuration
# 1. import the jwt (from flask_jwt_extended import JWTManager) 
# 2. Setup the Flask-JWT-Extended extension
# app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!

# # 3. Add when the authorization will expire: 
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)

# jwt = JWTManager(app) # instance of jwt 
# #4.  initialize the jwt 
# jwt.init_app(app)

#STEP 2 

#1. create go to views folder and create the auth file. 
#2. add the auth file to the __init__ py by importing. 

# 3. create a blue print in the auth. 

#4. create a blueprint for it : in the auth.py copy: 
# from flask import jsonify,request,Blueprint
# from backend.models import db,User

# auth_bp= Blueprint('auth_bp', __name__)

# 5. Create the login/ logout functions in the auth.py 

#PROTECT THE ROUTES: 
#Protected the with jwt_required, get_jwt_identity
# 5 To protect the route : jwt_required, get_jwt_identity: should be added in all the routes that need protections 

# 1. import: from jwt_extended import jwt_required, get_jwt_identity
    
@user_bp.route('/users', methods=["POST"])
# add the jwt_required decorator 
@jwt_required()
def add_users():
    data = request.get_json() 
    #current_user_id will get the user id. then we can remove anything related to user and replace it with current_user_id.
    current_user_id = get_jwt_identity()
    
    username = data['username']
    email = data['email']
    password = data['password']
    is_admin = data['is_admin']
    
#3. Check if the users/email exists

    current_user_id 
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





 


















    