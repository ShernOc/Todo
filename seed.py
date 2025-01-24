# Creates random data 
from faker import Faker
from models import User, Todo, Tag, db 
from app import app

#initialize 
fake = Faker()

def user_data():
    # Number of records to generate
    num_records = 15

    # Create random data
    
    with app.app_context():  
        try:
            for _ in range(num_records):
                user = User(
                # Replace with your model's fields,
                username=fake.user_name(),
                email=fake.email(),
                password = fake.password(),
                is_admin=fake.boolean(),
                is_approved=fake.boolean()
            )
                db.session.add(user)

            # Commit to the database
            db.session.commit()
            print(f"{num_records} Users added to the database!")
        except Exception as e:
            print("An error occurred:", e)
            db.session.rollback() 
        
def todo_data():
    # Number of records to generate
    num_records = 15
    
    with app.app_context():  
        try:
            # Fetch existing users and tags to create relationships
            users = User.query.all()
            tags = Tag.query.all()
    # Create random data
            for _ in range(num_records):
                todo = Todo(
                title=fake.sentence(nb_words=6),       
                # Replace with your model's fields
                description=fake.text(max_nb_chars=50),
                is_complete=fake.boolean(),
                deadline=fake.date_time_this_year().strftime("%d/%m/%Y"),
                user_id=fake.random_element(users).id,
                tag_id=fake.random_element(tags).id
                
            )
            db.session.add(todo)

            # Commit to the database
            db.session.commit()
            print(f"{num_records} records added to the database!")
        except Exception as e:
            print("An error occurred:", e)
            db.session.rollback() 
    
def tag_data():
    # Number of records to generate
    num_records = 15

    with app.app_context():  
    # Create random data
        try:
            for _ in range(num_records):
                tag = Tag(
                name=fake.name()      
            )
            db.session.add(tag)

            # Commit to the database
            db.session.commit()
            print(f"{num_records} records added to the database!")
        
        except Exception as e:
            print("An error occurred:", e)
            db.session.rollback() 
    
if __name__ == "__main__":
    user_data()
    todo_data()
    tag_data()
    