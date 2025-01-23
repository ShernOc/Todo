from flask import jsonify,request,Blueprint
from models import db,Tag
from flask_jwt_extended import jwt_required, get_jwt_identity

tag_bp= Blueprint('tag_bp', __name__)

#Fetch/Get Tags
#fetch all tags
@tag_bp.route('/tags')
# protect the route 
@jwt_required()
def get_tags():
    #query.all gets all the tags 
    # current_user_id = get_jwt_identity()
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
@tag_bp.route('/tags', methods=["POST"])
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
#you can update the name, password,email ..
@tag_bp.route('/tags/<tag_id>', methods = ['PATCH'])        
def update_tag(tag_id):
    tag = Tag.query.get(tag_id)
    
    #check if tag id exists 
    if tag: 
        data = request.get_json()
        name = data.get('name', tag.name)
        
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
@tag_bp.route('/tags/<int:id>')
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
@tag_bp.route('/tags/<int:tag_id>', methods = ["DELETE"])
def delete_tag(tag_id):
    #get all the data 
    tag = Tag.query.get(tag_id)
    
    if tag: 
        db.session.delete(tag)
        db.session.commit()
        return jsonify({"Success":"Tag deleted successfully"})
    
    else:
        return jsonify({"Error":"Tag does not exist"})
      