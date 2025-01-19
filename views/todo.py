


from flask import jsonify,request,Blueprint
from models import db,Todo, User, Tag
from datetime import datetime

todo_bp = Blueprint('todo_bp', __name__)

#================Todo=====SECTION === 
#fetch all todos
@todo_bp.route('/todos')
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
@todo_bp.route('/todos/<int:id>')
def fetch_one_todo(id):
    todo= Todo.query.get(id)
    
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
@todo_bp.route('/todos', methods= ['POST'])
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
@todo_bp.route('/todos/<todo_id>')
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
@todo_bp.route('/todos/<int:todo_id>', methods =['DELETE'])
def delete_todo(todo_id):
    #get the users
    todos = Todo.query.get(todo_id)
    if todos:
        db.session.delete(todos)
        db.session.commit()
        return jsonify({"Success Todo, successfully deleted"})

    else:
         return jsonify({"Error": "Todo does not exist, Try again"})
