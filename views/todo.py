from flask import jsonify,request,Blueprint
from models import db,Todo, User, Tag
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

todo_bp = Blueprint('todo_bp', __name__)

#================Todo=====SECTION === 
#fetch all todos
@todo_bp.route('/todos', methods = ['GET'])
@jwt_required()
def get_todo():
    current_user_id = get_jwt_identity()
    #get all the todos 
    # todos = Todo.query.all()
    # this will allow us generate todo based on user alone with the token 
    todos = Todo.query.filter_by(user_id = current_user_id)
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
@todo_bp.route('/todos/<int:id>')
@jwt_required()
def fetch_one_todo(id):
    current_user_id = get_jwt_identity()
    
    todo= Todo.query.filter_by(id, user_id = current_user_id).first|()
    if todo:
        return jsonify({
            "id":todo.id,
            "title":todo.title,
            "description":todo.description,
            "is_complete":todo.is_complete,
            "deadline":todo.deadline,
            "user_id":todo.user_id,
            "tag_id": todo.tag_id,
            #this allows you to fetch just the user/ based on the id, or the username
            "user":{"id":todo.user.id, "username":todo.user.username,}
        })
    else: 
        return jsonify({"Error":"Tag doesn't exist"})
    
  
#Add a todo list 
@todo_bp.route('/todos', methods= ['POST'])
#jwt_required added for checking the user id 
@jwt_required()
def add_todo():
    #add/ get the current_user_id = get_jwt_identity()
    current_user_id = get_jwt_identity()
    #initialize the data 
    data = request.get_json()
    title = data.get('title')
    description=data.get('description')
    # user_id=data.get('user_id') : removed now we only have to use current_user_id 
    
    tag_id= data.get('tag_id')
    try:
        deadline = datetime.strptime(data.get('deadline'), "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return jsonify({"error":"invalid datetime"})
    
    #check if they exist: 
    #removed because we dont need it
    # check_user_id = User.query.get(user_id)
    check_tag_id = Tag.query.get(tag_id)
    
    #if they dont exist, then 
    # if not check_user_id or not check_tag_id:
    if not check_tag_id:
        return jsonify({"Error": "Todo does not exist"}), 406
    
    else: 
        new_todo = Todo(title = title, description = description, 
        # user_id = user_id, removed to be user_id = current_user_id
        user_id = current_user_id,tag_id = tag_id, deadline = deadline)
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({"Success":"Todo added successfully" })
    
    
#Update a todo 
@todo_bp.route('/todos/<todo_id>')
@jwt_required()
def update_todos(todo_id):
    current_user_id = get_jwt_identity()
    #check if todo exists by query.get( which is a default using the get)
    todo= Tag.query.get(todo_id)
    data = request.get_json()
    
    # if todo is there with its user_id allow that user to update the todo
    #Thus: 
    
    if todo and todo.user_id == current_user_id: # if user exist
        #get the data 
        title = data.get('title', todo.title)
        description = data.get('description', todo.description)
        tag_id = data('tag_id', todo.tag_id)
        # user_id = data('user_id', todo.user_id)
        # is complete tells us if the todo is done 
        is_complete= data('is_complete', todo.is_complete)
        
        try:
            deadline = datetime.strptime(data.get('deadline', todo.deadline), "%Y-%m-%d %H:%M:%S")
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
            # removed because it's not needed. 
            # todo.user_id = user_id
            todo.is_complete = is_complete
        
        #calling the function
            db.session.commit()
            return jsonify({"success": "todo updated successfully"})
    else:
        return jsonify({"error":"todo doesn't exist or not authorized k"})
           
#DELETE Todo; 
@todo_bp.route('/todos/<int:todo_id>', methods =['DELETE'])
@jwt_required()
def delete_todo(todo_id):
    #get the users
    current_user_id = get_jwt_identity()
    # confirms if the delete is from the user. 
    todos = Todo.query.filter_by( id = todo_id, user_id = current_user_id)
    if todos:
        db.session.delete(todos)
        db.session.commit()
        return jsonify({"Success Todo, successfully deleted"})

    else:
         return jsonify({"Error": "Not authorized to delete"})
