from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Metadata

#What do they even mean? 
metadata = Metadata
db = SQLAlchemy(metadata= metadata)


#create the classes of the Todo app. 
#Create the tables: User, Tag, Todo
#User: username, email, password, 

class User(db.Model):
    id = db.Column
    


