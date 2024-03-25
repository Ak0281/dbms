from flask import Flask,render_template,redirect,request,session, url_for,flash,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
from sqlalchemy import text
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app)




#MY db connection
local_server=True
app = Flask(__name__)
app.secret_key='adityakarthikeyan'

login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/databas_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/wms'
db=SQLAlchemy(app)



#here we will create db models that is tables
class Test(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50),unique = True)
    password = db.Column(db.String(1000))
    role = db.Column(db.String(20))

    def __repr__(self):
        return f"<User {self.username}>"

class Research_Scholar(db.Model):
    __tablename__ = 'research_scholar'  # Specify the correct table name
    r_sid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    elevel = db.Column(db.String(50))
    rtopic = db.Column(db.String(50))
    specialization = db.Column(db.String(50))
    dept = db.Column(db.String(50))
    number = db.Column(db.String(12))

class Scientist(db.Model):
    __tablename__ = 'scientist'
    sid = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    number = db.Column(db.String(12))
    dept = db.Column(db.String(50))
    specialization = db.Column(db.String(50))
    rtopic = db.Column(db.String(50))

class wheat(db.Model):
    __tablename__ = 'wheat'
    wid = db.Column(db.Integer, primary_key=True)
    Genotypes = db.Column(db.String(50))
    R1_PH = db.Column(db.String(12))
    R2_PH = db.Column(db.String(12))
    R3_PH = db.Column(db.String(12))
    R1_TPP = db.Column(db.String(12))
    R2_TPP = db.Column(db.String(12))
    R3_TPP = db.Column(db.String(12))
    R1_DFF = db.Column(db.String(12))
    R2_DFF = db.Column(db.String(12))
    R3_DFF = db.Column(db.String(12))
    R1_SPAD = db.Column(db.String(12))
    








@app.route('/')
def index():
    return render_template('index.html')



@app.route('/Scientist', methods=['POST', 'GET'])
@login_required
def scientist():
    if current_user.role != 'scientist':  # Check if the current user is a research scholar
        flash("You do not have permission to access this page", "danger")
        return redirect(url_for('index'))
    if request.method == "POST":
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        number = request.form.get('number')
        dept = request.form.get('dept')
        specialization = request.form.get('specialization')
        rtopic = request.form.get('rtopic')
        

        # Define the SQL query
        sql_query = text("INSERT INTO scientist (fname, lname, email, number, dept, specialization, rtopic) VALUES ( :fname, :lname, :email, :number, :dept, :specialization, :rtopic)")

        # Execute the SQL query with parameters
        db.session.execute(sql_query, {'fname': fname, 'lname': lname, 'email': email, 'number': number, 'dept': dept, 'specialization': specialization, 'rtopic': rtopic})

        # Commit the transaction
        db.session.commit()

        flash("Submission Confirmed", "info")
        return render_template('scientist.html')

    return render_template('scientist.html')


@app.route('/research', methods=['POST', 'GET'])
@login_required
def research():
    if current_user.role != 'research_scholar':  # Check if the current user is a research scholar
        flash("You do not have permission to access this page", "danger")
        return redirect(url_for('index'))
    if request.method == "POST":
        email = request.form.get('email')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        specialization = request.form.get('specialization')
        gender = request.form.get('gender')
        dept = request.form.get('dept')
        rtopic = request.form.get('rtopic')
        elevel = request.form.get('elevel')
        number = request.form.get('number')
        sql_query = text("INSERT INTO research_scholar (email, fname, lname, gender, specialization, dept, rtopic, elevel, number) VALUES (:email, :fname, :lname, :gender, :specialization, :dept, :rtopic, :elevel, :number)")
        db.session.execute(sql_query, {'email': email, 'fname': fname, 'lname': lname, 'gender': gender, 'specialization': specialization, 'dept': dept, 'rtopic': rtopic, 'elevel': elevel, 'number': number})
        db.session.commit()
        flash("Booking Confirmed", "info")
        return render_template('research.html')
    return render_template('research.html')

@app.route('/rtable')
@login_required
def rtable():
    em = current_user.email
    
    # Query the Research_Scholar table for the current user's data
    query = Research_Scholar.query.filter_by(email=em).all()
    
    # Pass the query result to the template during rendering
    return render_template('rtable.html', query=query)

@app.route('/edit/<string:r_sid>', methods=['GET', 'POST'])
def edit_research(r_sid):
    post = Research_Scholar.query.filter_by(r_sid=r_sid).first()
    if request.method == "POST":
        email = request.form.get('email')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        specialization = request.form.get('specialization')
        gender = request.form.get('gender')
        dept = request.form.get('dept')
        rtopic = request.form.get('rtopic')
        elevel = request.form.get('elevel')
        number = request.form.get('number')
        
        try:
            # Update the post in the database
            post.email = email
            post.fname = fname
            post.lname = lname
            post.specialization = specialization
            post.gender = gender
            post.dept = dept
            post.rtopic = rtopic
            post.elevel = elevel
            post.number = number
            
            # Commit the changes
            db.session.commit()
            
            flash("Update Successful", "success")
            return redirect(url_for('rtable'))
        except Exception as e:
            flash(f"Update Failed: {str(e)}", "danger")

    return render_template('edit.html', post=post)

@app.route("/delete_research/<int:r_sid>", methods=['POST', 'GET'])
@login_required
def delete_research_record(r_sid):
    record = Research_Scholar.query.get_or_404(r_sid)
    try:
        # Delete the record
        db.session.delete(record)
        db.session.commit()
        flash("Record deleted successfully", "success")
    except Exception as e:
        flash(f"Error deleting record: {str(e)}", "danger")
    return redirect(url_for('rtable'))

@app.route('/stable')
@login_required
def stable():
    em = current_user.email
    
    # Query the Research_Scholar table for the current user's data
    query = Scientist.query.filter_by(email=em).all()
    
    # Pass the query result to the template during rendering
    return render_template('stable.html', query=query)

@app.route('/edits/<string:sid>', methods=['GET', 'POST'])
def edit_scientist(sid):
    post = Scientist.query.filter_by(sid=sid).first()
    if request.method == "POST":
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        number = request.form.get('number')
        specialization = request.form.get('specialization')
        dept = request.form.get('dept')
        rtopic = request.form.get('rtopic')
        
        try:
            # Update the post in the database
            post.fname = fname
            post.lname = lname
            post.email = email
            post.number = number
            post.specialization = specialization
            post.dept = dept
            post.rtopic = rtopic
            
            # Commit the changes
            db.session.commit()
            
            flash("Update Successful", "success")
            return redirect(url_for('stable'))
        except Exception as e:
            flash(f"Update Failed: {str(e)}", "danger")

    return render_template('edits.html', post=post)

@app.route("/delete_Scientist/<int:sid>", methods=['POST', 'GET'])
@login_required
def delete_scientist_record(sid):
    record = Scientist.query.get_or_404(sid)
    try:
        # Delete the record
        db.session.delete(record)
        db.session.commit()
        flash("Record deleted successfully", "success")
    except Exception as e:
        flash(f"Error deleting record: {str(e)}", "danger")
    return redirect(url_for('stable'))





@app.route('/add_wheat', methods=['POST', 'GET'])
@login_required
def add_wheat():
    if request.method == "POST":
        Genotypes = request.form.get('Genotypes')
        R1_PH = request.form.get('R1_PH')
        R2_PH = request.form.get('R2_PH')
        R3_PH = request.form.get('R3_PH')
        R1_TPP = request.form.get('R1_TPP')
        R2_TPP = request.form.get('R2_TPP')
        R3_TPP = request.form.get('R3_TPP')
        R1_DFF = request.form.get('R1_DFF')
        R2_DFF = request.form.get('R2_DFF')
        R3_DFF = request.form.get('R3_DFF')
        R1_SPAD = request.form.get('R1_SPAD')

        
        

        # Define the SQL query
        sql_query = text("INSERT INTO wheat (Genotypes, R1_PH, R2_PH, R3_PH, R1_TPP, R2_TPP, R3_TPP, R1_DFF, R2_DFF, R3_DFF, R1_SPAD) VALUES ( :Genotypes, :R1_PH, :R2_PH, :R3_PH, :R1_TPP, :R2_TPP, :R3_TPP, :R1_DFF, :R2_DFF, :R3_DFF, :R1_SPAD)")

        # Execute the SQL query with parameters
        db.session.execute(sql_query, {'Genotypes': Genotypes, 'R1_PH': R1_PH, 'R2_PH': R2_PH, 'R3_PH': R3_PH, 'R1_TPP': R1_TPP, 'R2_TPP': R2_TPP, 'R3_TPP': R3_TPP, 'R1_DFF': R1_DFF, 'R2_DFF': R2_DFF, 'R3_DFF': R3_DFF, 'R1_SPAD': R1_SPAD})

        # Commit the transaction
        db.session.commit()

        flash("Submission Confirmed", "info")
        return render_template('add_wheat.html')
    return render_template('add_wheat.html')

@app.route('/wtable')
@login_required
def wtable():
    query = wheat.query.all()
    
    
    # Pass the query result to the template during rendering
    return render_template('wtable.html', query=query)

@app.route('/dit/<int:wid>', methods=['GET', 'POST'])
def dit_wheat(wid):
    post = wheat.query.filter_by(wid=wid).first()
    if request.method == "POST":
        Genotypes = request.form.get('Genotypes')
        R1_PH = request.form.get('R1_PH')
        R2_PH = request.form.get('R2_PH')
        R3_PH = request.form.get('R3_PH')
        R1_TPP = request.form.get('R1_TPP')
        R2_TPP = request.form.get('R2_TPP')
        R3_TPP = request.form.get('R3_TPP')
        R1_DFF = request.form.get('R1_DFF')
        R2_DFF = request.form.get('R2_DFF')
        R3_DFF = request.form.get('R3_DFF')
        R1_SPAD = request.form.get('R1_SPAD')
        
        try:
            # Update the post in the database
            post.Genotypes = Genotypes
            post.R1_PH = R1_PH
            post.R2_PH = R2_PH
            post.R3_PH = R3_PH
            post.R1_TPP = R1_TPP
            post.R2_TPP = R2_TPP
            post.R3_TPP = R3_TPP
            post.R1_DFF = R1_DFF
            post.R2_DFF = R2_DFF
            post.R3_DFF = R3_DFF
            post.R1_SPAD = R1_SPAD
            
            # Commit the changes
            db.session.commit()
            
            flash("Update Successful", "success")
            return redirect(url_for('wtable'))
        except Exception as e:
            flash(f"Update Failed: {str(e)}", "danger")

    return render_template('dit.html', post=post)

@app.route("/delete_wheat/<int:wid>", methods=['POST', 'GET'])
@login_required
def delete_wheat_record(wid):
    record = wheat.query.get_or_404(wid)
    try:
        # Delete the record
        db.session.delete(record)
        db.session.commit()
        flash("Record deleted successfully", "success")
    except Exception as e:
        flash(f"Error deleting record: {str(e)}", "danger")
    return redirect(url_for('wtable'))



@app.route('/signup',methods = ['POST','GET'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')  # Get the role from the form
        user = User.query.filter_by(email=email).first()
        if user:
            flash("email already exists", "warning")
            return render_template('/signup.html')
        encpassword = generate_password_hash(password)
        new_user = User(username=username, email=email, password=encpassword, role=role)  # Set the role
        db.session.add(new_user)
        db.session.commit()
        flash("Signup Success please Login", "success")
        return render_template('login.html')
    return render_template('signup.html')

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","primary")
            return redirect(url_for('index'))
        else:
            flash("invalid credentials","danger")
            return render_template('login.html')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout Successfull","warning")
    return redirect(url_for('login'))


# Set cache control headers for static files
@app.route('/static/<path:path>')
@cache.cached(timeout=3600)  # Cache files for 1 hour (3600 seconds)
def send_static(path):
    return send_from_directory('static', path)




@app.route('/test.html')
def test():
    try:
        Test.query.all()
        return 'my db is connected'
    except:
        return 'my db is not connected'

    


app.run(debug=True)