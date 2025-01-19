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
#fetch all tags
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
    

#fetch one tag 
@app.route('/tags/<int:id>')
def fetch_one_tag(id):
    tagz= Tag.query.get(id)
    
    if tagz:
        return jsonify({
            "id":tagz.id,
            "name":tagz.name
        })
    else: 
        return jsonify({"Error":"Tag doesn't exist"})
    
#Delete Tag: 
from datetime import datetime
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
      
# =================Todo=====SECTION === 
#fetch all todos
@app.route('/todos')
def get_todo():
    #get all the todos 
    todos = Todo.query.all()
    #create an empty list of tod 
    todo_list = []
    
    for todo  in todos:
        todo_list.append({
            "id":todo.id,
            "title":todo.title,
            "description":todo.description,
            "is_complete":todo.is_complete,
            "deadline":todo.deadline,
            "user_id":todo.user_id,
            "tag_id": todo.tag_id
        }
        )
    
    return jsonify({"Todo-List ": todo_list})

#fetch one Todo based on id 
@app.route('/tags/<int:id>')
def fetch_one_todo(id):
    todo= Tag.query.get(id)
    
    if todo:
        return jsonify({
            "id":todo.id,
            "title":todo.title,
            "description":todo.description,
            "is_complete":todo.is_complete,
            "deadline":todo.deadline,
            "user_id":todo.user_id,
            "tag_id": todo.tag_id,
        })
    else: 
        return jsonify({"Error":"Tag doesn't exist"})
    
#Add a todo list 
@app.route('/todos', methods= ['POST'])
def add_todo():
    #initialize the data 
    data = request.get_json()
    title = data['title']
    description=data['description']
    user_id=data['user_id']
    tag_id= data['tag_id']
    try:
        deadline = datetime.strptime(data['deadline'], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return jsonify({"error":"invalid datetime"})
    
    #check if they exist: 
    check_user_id = User.query.get(user_id)
    check_tag_id = Tag.query.get(tag_id)
    
    #if they dont exist, then 
    if not check_user_id or not check_tag_id:
        return jsonify({"Error": "Todo does not exist"}), 406
    
    else: 
        new_todo = Todo(title = title, description = description, user_id = user_id, tag_id = tag_id, deadline = deadline)
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({"Success":"Todo added successfully" })
    
    
#Update a todo 
@app.route('/todos/<todo_id>')
def update_todos(todo_id):
    #check if todo exists by query.get( which is a default using the get)
    todo= Tag.query.get(todo_id)
    
    if todo: # if user exist
        #get the data 
        data = request.get_json()
        title = data['title']
        description = data['description']
        tag_id = data['tag_id']
        user_id = data['user_id']
        try:
            deadline = datetime.strptime(data['deadline'], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return jsonify({"error":"invalid datetime"})
    
        check_title = Todo.query.filter_by(title = title).first()
        check_description = Todo.query.filter_by(description = description).first()

        if check_title or check_description:
            return jsonify({"error": "title/description already exist"})
        else:
            todo.title = title
            todo.description = description
            todo.tag_id = tag_id
            todo.deadline = deadline
            todo.user_id = user_id
        
        #calling the function
            db.session.commit()
            return jsonify({"success": "todo updated successfully"})
    else:
        return jsonify({"error":"todo doesn't exist"})
           
#DELETE Todo; 
@app.route('/todos/<int:todo_id>', methods =['DELETE'])
def delete_todo(todo_id):
    #get the users
    todos = Todo.query.get(todo_id)
    if todos:
        db.session.delete(todos)
        db.session.commit()
        return jsonify({"Success Todo, successfully deleted"})

    else:
         return jsonify({"Error": "Todo does not exist, Try again"})
