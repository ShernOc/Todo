from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

#
# from sqlalchemy_serializer import SerializerMixin
# class User(db.Model, SerializerMixin):


#What do they even mean? 
metadata = MetaData()
db = SQLAlchemy(metadata= metadata)

#Create the tables class : User, Tag, Todo using the Model method

#User table:
#User: username, email, password, 
class User(db.Model):
    #named the table Users 
    __tablename__ = "Users"
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(128), nullable = False)
    email = db.Column(db.String(128),nullable =False)
    is_approved = db.Column(db.Boolean, default = False)
    password = db.Column(db.String(120), nullable = False)
    
    # Another section is created for an admin  in models: for adming 
    #ADMIN 
    is_admin = db.Column(db.Boolean, default = False)
    
    #apply to migration: flask db migrate"add admin field", 
    
    #FETCHING PURPOSE 
    #create a relationship with the Todo Table
    #Allows us to create a fetching 
    todos = db.relationship("Todo",back_populates="user", lazy =True)
    
    #repr methods returns a string
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.is_approved}',{self.password} ,{self.todos})" 
    
# Tag Table
class Tag(db.Model,):
    __tablename__ = "Tags"
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(128), nullable=False)

    #Create a relationship
    todos = db.relationship("Todo", back_populates ="tag", lazy= True)
    
    def __repr__(self):
        return f"Tag('{self.name}')"
    
# To-do table :  
class Todo(db.Model):
    __tablename__ = "Todos"
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(128), nullable = False)
    description = db.Column(db.String(256))
    is_complete= db.Column(db.Boolean, default = False)
    deadline = db.Column(db.String(20), nullable = False)
    
    #create a relationship 
    user_id = db.Column(db.Integer,db.ForeignKey("Users.id"), nullable= False)
    tag_id = db.Column(db.Integer,db.ForeignKey("Tags.id"), nullable= False)
    # Relationships
    user = db.relationship("User", back_populates="todos")
    tag = db.relationship("Tag", back_populates="todos")
    
    
    def __repr__(self):
        return f"Users('{self.title}', '{self.description}', '{self.is_complete}',{self.deadline} ,{self.user_id}, {self.tag_id})"
    
    
    #Logout Flask Model 
class TokenBlocklist(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        jti = db.Column(db.String(36), nullable=False, index=True)
        created_at = db.Column(db.DateTime, nullable=False)
    
    

     
    
    
    

    
    
    
    
    


