#FLASK NOTES: 

#Update user 
#Delete User 

# @app.route('/todo')
# #Receive the data in json 
# def add_todo():
#     data = request.get_json()
       
# #Run the application: 
# if __name__ == '__main__':
#     app.run(port=5555, debug=True)
    
# # #To add 
# # user = User()
# # db.session.add(user)
# # db.session.commit()


# # #To update/modify data 
# # user.verified = True
# # db.session.commit()

# # #to delete
# # db.session.delete(user)
# # db.session.commit()


#Add a Users/ Add you use the method POST 
#1. Receive the data in json: 
#To add ? you have to check if the user first exists, if yes you create an error message that the user exist, if not you add the user 
#2. You initialize: data = request.get_json()
    
#3. Check if the users exists by using filter_by or filter(username)

#4. create an error message if the username or email exists, if yes: return an error message 200/ is just an indication of the error
    #prints the output
    
#5. Next you now update/by calling the db.session.add(new_user) db.session.commit()

#6 return jsonify({Successfully})

#Connect to the Postman
#Connect to the POSTMAN
#1. Copy the Url http://127.0.0.1:5000


#   QUESTIONS
#How to update just the name? 
#How to 




    