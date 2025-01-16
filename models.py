from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import MetaData

#What do they even mean? 
metadata = MetaData
db = SQLAlchemy(metadata= metadata)




#create the classes of the Todo app. 
#Create the tables: User, Tag, Todo
#User: username, email, password, 

class User(db.Model):
    id = db.Column
    


