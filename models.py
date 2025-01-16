from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import MetaData

#What do they even mean? 
metadata = MetaData()
db = SQLAlchemy(metadata= metadata)

#create the classes of the Todo app. 

#Create the tables: User, Tag, Todo using the Model method

#User table:
#User: username, email, password, 
class User(db.Model):
    #named the table Users 
    __tablename__ = "Users"
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(128), nullable = False)
    email = db.Column(db.String(128),nullable =False)
    is_approved = db.Column(db.Boolean, default = False)
    password = db.Column(db.String(128), nullable = False)
    
    #create a relationship with the Todo Table
    todo = db.relationship("Todo",backref="user", lazy = True)
    
    #repr methods returns a string
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.is_approved}',{self.password} ,{self.todo})" 
    
# Tag Table
class Tag(db.Model):
    __table__ = "Tag"
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(128), nullable=False)

    #Create a relationship
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"),nullable = False)
    
    def __repr__(self):
        return f"User('{self.name}', '{self.user_id}')"
    
# To-do table :  
class Todo(db.Model):
    __table__ = "Todo"
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Colum(db.String(128), nullable = False)
    description = db.Column(db.String(256))
    is_complete= db.Colum(db.Boolean, default = False)
    deadline = db.Column(db.String(20), nullable = False)
    
    #create a relationship 
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"), nullable= False)
    tag_id = db.Column(db.Integer,db.ForeignKey("tag.id"), nullable= False)
    
    def __repr__(self):
        return f"User('{self.title}', '{self.description}', '{self.is_complete}',{self.deadline} ,{self.user_id}, {self.tag_id})"
    
    
    

    
    
    
    
    


