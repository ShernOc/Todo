1. Be able to 
2. Install Flask, Flask-SQL, Flask-Migrate, 
3. Something about the Blueprint 


a. Create tables for User, Todo, Tag
b. In the User be able to 
- Add a User
-Update a User
-Delete a user

c. In the Tag
- Add a Tag 
- Update a Tag
- Delete a Tag

d. In the Todo 
- Add a Todo
-Update a Todo
- Delete a Todo 




#VITE/TAILWIND INSTALLATION

1. Create a front-end folder 
Install react application with vite/tailwind
2. REACT COMPONENTS:
- create the files
- import the apps in app.py
app.jsx
download the react-dom

=
 - <Route>
  <route path>


  datetime: 
  
  The datetime class requires at least three arguments: year, month, and day. You provided only one argument: data['date'].



Tuesday: 21/01/2024 

function for for todo: 
1. import {createCOntext} from react 
- Create a TodoCOntext.jsx
-UserContext.jsx

export const TodoContext =
2. Create all the fuctions addTodo: 
const addTodo (user.id){
    return: 
    console.log(data)
} 

2. const data= { 
    getTags, 
    addTodo,
    updateTodo
    DeleteTodo 
}

3. Go to router 
<UserProvider>
<Todo_Provider>
<Routes>
<Todo_Provider> # everything between the route will have acccess of the document 

4. Now use: To Access the work 
const {addUser} = UseContext()

cors error: trying to communicate between two errors: 
flask cors: import it: pipenv install  flask cors 

- app.pypy 
- import : from flask_cors import CORS 
 # - initialize it 
CORS(app)
json place holder?? : Use it for react template heading/ learning getting: /??

6. The message should should be displayed in the browser. 
-toastify?? 
import toastify: pipenv install toastify: 
import (ToastContainter) from react-toastify
<ToastContainer> add it at the Layout, or anywhere: 

Connect: 

Login: You recieve the token in the browser: 
- save the token in the browser: 
paste the toast.loading to the login section: 
- const login(email,password)
- we have two tokens in auth.py: 
response_access_token: 
if (resposonse.access_token){
    toast.dismiss()
    toast.success
}

4. Go to login: 
cont {login} = UseContext 
if successful: 
login(email,password)

5. Save the Token to the browser: 
#save and retrieve the token : https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage

- section scoren: more secure 
- local storage: : 
localStorage.setItem("myCat", "Tom");
SessionStorage.setItem() # the token is saved 

6. Using the token: everytime
: const authToken, setAuthToken = useState()=> sessionStorage.getItem()

#need to utilise 

Copy: sessinStorage: The auth gets append again. 
:We have the token: for the 2hrs for the login: 

#fetch_current User: 
authorization: barrier is also passed: 
Authorization: only where the user i needed. 
Authorization : "Barrier ${authToken}
#call the authorization where imediately where the user has logged in. 

at the const login = ()

-TODO
- Have two fetches: 
1. when user is login .
2. When the user is inside the function

#current user needs to be on a news state value: 
const(currentuser,)
setCurrent User to be response: 

- Use the UseEffect: ()= CurrentUser: 
if current user: else: 
-When you log of you need to nullify: 
-    setCurrentUser(null)
- 

-Login,Logout, 

Wednesday: 
TodoContext Challenge: allows you to access anything related to something. To access the data from context you need to have 
TodoProvider: router have access to everything withing the TodoProvider. 
- UserProvide: has access the authentication. 
-Browser Router: Has to be the highest form of codding. 

2. UserContext
    - Add User: 
    -toast: React Package:  react-toastify: download it. 
    - Installing the toast: 
        - go to layout: import {ToastContainer}
        return jsonify: is a response: You 
        response is an object. 
        - If (response.msg): 
    Session.Storage: being able to save the 

-To protect the Routes: 
    - Profile:  email, is_approved, is_admin, 
    - Getting the const{current_User} = UseContext(UserContext): # This allows you to access the current_User. 
 - &&: will display empty if the current User is not empty- CurrentUser.username) # allows one to display something. 


 2. Approval Statement: 
 inside the approval:  
{
    current_user && current_user.is_approved ?  "Approved": "Pending Approved" 
}

if user is admin: 
current_user && current_user.is_admin?
"Admin": "User": 

#Being able to edit 
# SQQLIti3 editor: open with: Sqlite 3: 
: 
    - You can have a Super Admin, or Admin: 


# Componenst: 
Home, Login, Profile, Register/Create , SingleTodo, AddTodo, NoPage.jsx: 

    ${current_user && current_user.is_admin?" text-blue-900: orange }
 
    How to navigate the page if not current user 
 #1. if not current user: 
 if (!current_user){
    navigate('/login)
}

# PROTECT THE ROUTES: 
 #This protect the router from being displayed: 
 (!current_user_user? "Not Authorized)

# 3. Add Todo = TodoContext.jsx : 
without @jwt_required: There is a need for authorization. 

 1. Fetch the Tags first : No authorization needed. 
 - At the Add_To_Do
 cons{tags} = UseContext(TodoContext) # passing it from the TodoContext
 - 1. How do you fetch the Tags
    - Use the UseEffects 
    useEffects(()=>)
- Create a Drop down Tag that is needed: 
    -  Tag
    <Select Onchange = (e).target.value >
<select> {tags && tags.map(()=>(
    <Options value = {tag.id} key={tag.id}>{tag.name}</Optons>
)
)}

; Date selected should not below the date. 

2. How do we now display : 
    -Tag id: should be an integer. 
    -Success and error: those are the responses 
# how to access the current user 
    const {authToken} = UseContext(UserContext)
    - You need to call the add todo 
   const addtodo(tite, description,closure,)
   call it 
   addtodo(
   )
parseint(tat_id) : change string to integer
# You have to call it at the token 

- const data{
    authtoken 
}

SetDeadline("")
SetDescription("SetDeadline" to be empty)
set

#Add to do, should should have a authentication. 

# FETCH TO DO 
- Token has to be passed


UseEffect(()=>{
    fetch(), {
        methods
    }
    .them((response )= response.json()
    then(response ))
})

const data{
    todo,
    tags,
    addTodo

}
- HomePage displays the todo
 - const {todos}= UseContext(TodoContext)(
    return 
    current user? 

    <div>
    { # curly brackets are used for javacode inside a react 

    todos && todo.lengh < 1 && 
    div >
     You dont have Todos 
     add a link for  <Link to = "/addtodos"> Created
    }
    todos && todo.map && todos.map(todo)=>(
        key={tod.id}>,
        hi> {todo.title}
        <p> {todo.deadline} </p>
    )
 )


# THUSDAY 23/01/2025
- Import {AuthContext} from '..Context/AuthoContext 

    - remember to have the links:
-Protecting the Route 

# To make a Colums/Table For Table. 
- Enclose the use the crid. 
- Go to Tailwind (grid_template_Columns)
        - grind cols-4 gap-4 
# How to access the Tag 
{todo.tag.name} # next style it.

# Flex: To be in one line: 
justify-between, 

#vertivally: items-center 
text-right: on the right corner 
text-xs: Text to be small 

is_complete()
#have in a different paragraph with className= 
{
todo.is_complete ? # message ("Completed") : ("Not Complete")}

arrow function <span>Onclick

# DELETE: UseState: 
- const Onchange, SetOnchange = SetState(false); 
# 
- Go to the add if its success: change it from false to true: 
setOnchange({!OnChange}) ; negates the value to be false. 

- 
dynamic route 
Route path "todo/:id"
Link: to= {/todo/$tod.id} # direct to a single todo page. 


Single: Todo: 
useparam from react-router-dom

1. filter the todo you already have 
return (
const{id} = UseParam()
const {todo}=UseContext(TodoContext)
const todo = {todo && todo.find((todo)=>todo.id==id)

return 
!todo && "Todo not found 
)


#Add a description: 
 Access the delete: 
 delete: to navigate to the homepage 
 / initializec 
 const onchnage 


# HOMEWORK: 
#UPDATE: the profile, 
#Add a button: For deleting an Account: 
# Chosing the projects: 

 # Update/ Add are thE Same; the Session, 
 # Need to Deploy the Page: 

#Homework: 
 #Choose the project: 
 #Code Challenge
 # Homework 
 # Wk2 Day 10 : Pizza Resturant Homework : 





    
#backref: one to many relationship cohort: students