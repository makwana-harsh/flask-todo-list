from flask import Flask,render_template,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "This_is_secret_key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MOODIFICATIONS']=False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mobile = db.Column(db.String(10), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)
    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    task = db.Column(db.String(200), nullable=False)
    # status = db.Column(db.String(20), default = "Pending")  # jinja code for status => {% comment %} - Status: {{ task.status }} {% endcomment %}  
    # due_date = db.Column(db.DateTime, nullable=True)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods = ["GET","POST"])
def register():
    if request.method == "POST":
        uName = request.form["u_name"]
        emailId = request.form["email_id"]
        mobileNo = request.form["mobile_no"]
        dob = request.form["d_o_b"]
        password = bcrypt.generate_password_hash(request.form["password"]).decode("utf-8")
        
        existing_user = User.query.filter_by(username=uName).first()
        if existing_user:
            return "Username already exists! Try another one."
        
        user = User(username=uName, email=emailId, mobile=mobileNo, dob=dob, password=password)
        db.session.add(user)
        db.session.commit()
        
        return redirect("/login")
        
    return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uName = request.form["u_name"]
        password = request.form["password"]
        
        user = User.query.filter_by(username=uName).first()
        if user and bcrypt.check_password_hash(user.password,password):
            session["user_id"] = user.id
            session["username"] = user.username
            return redirect("/tasks")
        return "Invalid credentials!"
    return render_template("login.html")

@app.route('/tasks')        #used to list all the tasks of user
def tasks():
    if "user_id" not in session:
        return redirect('/login')
    user_tasks = Task.query.filter_by(user_id=session["user_id"]).all()
    return render_template("tasks.html", tasks=user_tasks) 
    
@app.route("/add_task", methods=["POST"])       # used to ADD tasks of user
def add_task():
    if "user_id" not in session:
        return redirect("/login")
    
    new_task = Task(user_id=session["user_id"], task=request.form["task"])
    db.session.add(new_task)
    db.session.commit()
    
    return redirect("/tasks")

@app.route("/delete_task/<int:task_id>")      # used to DELETE tasks of user
def delete_task(task_id):
    if "user_id" not in session:
        return redirect("/login")
    Task.query.filter_by(id=task_id, user_id=session["user_id"]).delete()
    db.session.commit()
    
    return redirect('/tasks')

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
     
@app.route('/aboutUs')
def aboutUs():
    return render_template('aboutUs.html')



if __name__ == '__main__':
    app.run(debug=True)

