from flask import jsonify,request,Blueprint
from models import db,User,TokenBlocklist
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt

#time from jwt 
from datetime import datetime
from datetime import timedelta
from datetime import timezone

auth_bp= Blueprint('auth_bp', __name__)

# Create the login/logout blueprint functions

#login 
@auth_bp.route('/login', methods= ["POST"])
#we want to get the data from the user( email,password) 
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    # check if we have the user already exist in the database 
    user = User.query.filter_by(email=email).first()
    
    #check if password_hash by importing : from werkzeug.security import generate_password_hash
    #if user exist and check password hash, and password from the user, and database create a Token
    #check_-password_hash( takes two arguments)
    
    #Create Access Token
    #CREATE TOKEN: 
    #Access token is like a password: 
    #1. import : from flask_jwt_extended import create_access_token
    #Next import the create 
    #    access_token = create_access_token(pass a value ) :
    #NB: Token is linked to a specific user: (identity=user.id)
    # 3. Next you now return in 
    # return jsonify({"access_token":access_token})
    
    # remember each token is linked to a user: they have different token
    if user and check_password_hash(user.password , password):
        access_token = create_access_token(identity= str(user.id))
        # return jsonify({"Success": "Success done"})
        return jsonify({"access_token":access_token}), 200
    
        # return jsonify({"Success": "Correct submission"}), 200
    else: 
        return jsonify({"Error": "No authentication Its a Scam"}), 404
    
    
    # Next go to Postman and add a Login request 

    #NEXT: GETTING THE CURRENT USER 
    # 1. Pass the token 
    # 2. protecting the route. 
    #     - import the jwt_required 
    # 3. create a current_user route ()
@auth_bp.route('/current_user', methods = ['GET'] )
  #Protect the route we use @jwt_required decorator, for any route that need protection.
@jwt_required()
def current_user(): 
    # to get the current user we use the get_jwt_identity. 
    # dont forget to import it.
    current_user_id =get_jwt_identity()
    
    # to get the current user
    user = User.query.get(current_user_id)
    
    # Go to what is needed to be filled from a User: 
    user_data = [{
            "id": user.id,
            "email":user.email,
            "username":user.username,
            "email":user.email, 
            "is_approved":user.is_approved,
            "is_admin":user.is_admin}]
    
    return jsonify({"Current_user": user_data}),200
    
    # print(current_user_id) # 
    #You have to pass the token to the jwt_required
    
    # Pass: Copy the token:Go to authorization- And Go to the Bearer Token and Paste the Token.     
    
    
    
 #logout function 
 # Go to jwt_revoke: 
 # create a blocklist table for the logout. in the Model
 # Have a callback function and copy it tothe app.py: to check if the app is revoked. 
 # Go to the  
#  - import the datetime, TokenBlocklist, (import datetime, TokenBlocklist from models )

@auth_bp.route("/logout", methods=["DELETE"])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)
    db.session.add(TokenBlocklist(jti=jti, created_at=now))
    db.session.commit()
    return jsonify({"Success": "Logout successfully"})




