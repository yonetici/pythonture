from flask import Flask, render_template, escape, flash, redirect, url_for, session, logging, request, g
import sqlite3 as sql
from wtforms import Form, StringField, BooleanField, TextAreaField,PasswordField, validators
import hashlib 
from functools import wraps 

#Kullanıcı giriş decorate
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfayı görüntüleme yetkiniz yok", "danger")
            return redirect(url_for("login"))
    return decorated_function
#kullanıcı kayıt formu
class RegisterForm(Form):
    name = StringField("İsim Soyisim", validators=[validators.Length(min=4, max=25), validators.DataRequired()])
    username = StringField("Kullanıcı Adı", validators=[validators.Length(min=4, max=25), validators.DataRequired()])
    email = StringField("E-mail Adresiniz", validators=[validators.Email(message = "Geçerli bir mail adresi yazın.")])
    password = PasswordField("Parola", validators=[
        validators.DataRequired(message = "Lütfen bir parola belirleyin"),
        validators.EqualTo(fieldname = "confirm", message="Parola eşleşmiyor.")
    ])
    confirm = PasswordField('Şifreyi tekrar yazın')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

class LoginForm(Form):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Parola")
app = Flask(__name__)
app.secret_key = "ybblogSAAS^'+"
DATABASE = 'blog.db'
# try:
#     def connect_db():
#         return sql.connect(DATABASE)
    
# except:
#     print("hata")

# @app.before_request
# def before_request():
#     g.db = connect_db()

# @app.teardown_request
# def teardown_request(exception):
#     if hasattr(g, 'db'):
#         g.db.close()


@app.route("/")
def index():
    numbers = [
        {"id":1, "title":"DenemeTitle1","content":"DenemeContent1"},
        {"id":2, "title":"DenemeTitle2","content":"DenemeContent2"},
        {"id":3, "title":"DenemeTitle3","content":"DenemeContent3"}
    ]
    return render_template("index.html", numbers = numbers)
@app.route("/about")
def about():
    return render_template("about.html")
# @app.route("/article/<id>")
# def detail(id):
#     try:
#         return 'Post %s' % escape id
#     except:
#         return 'hatalı url girdiniz.'
@app.route('/article/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    try:
        return 'Post %d' % post_id
    except:
        return 'hatalı url girdiniz.'
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)
#Makale Ekle
class ArticleForm(Form):
    title = StringField("Makale Başlığı", validators=[validators.Length(min = 5, max= 100)])
    content = TextAreaField("Makale İçeriği", validators=[validators.Length(min = 5)])
@app.route("/addarticle", methods=['GET','POST'])
@login_required
def addarticle():
    form = ArticleForm(request.form)
    return render_template("addarticle.html", form = form)
@app.route('/register', methods=['GET', 'POST'])
def kayit():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        with sql.connect("./blog.db") as con:
            cur = con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS busers (
        	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	        "name"	TEXT,
	        "email"	TEXT,
	        "username"	TEXT UNIQUE,
            "password" TEXT
            )''')
# CREATE TABLE IF NOT EXISTS busers (
# 	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
# 	"name"	TEXT,
# 	"email"	TEXT,
# 	"username"	TEXT UNIQUE,
#   "password" TEXT
# )
        try:        
            name = form.name.data
            username = form.username.data
            email = form.email.data
            passwo = form.password.data
            #password = bcrypt.hashpw(passwo.encode('utf8'), bcrypt.gensalt())
            password = hashlib.md5(passwo.encode()).hexdigest()
            #cur.execute('''INSERT INTO busers (name, email, username, password) VALUES (?, ?, ?, ?)''', (name, email, username, password))
    #              cur.execute('INSERT INTO busers (name, email, username, password) VALUES (?, ?, ?, ?)', (name, email, username, password))            
            cur.execute("INSERT INTO busers (name, username, email, password) VALUES (?, ?, ?, ?)", (name, username, email, password))
            
            con.commit()
            msg = True
        except sql.IntegrityError as e:
            con.rollback()
            #'sqlite error: ', e.args[0]
            msh = False

            #msg = "error in insert operation"
      
        finally:
         #return render_template("result.html",msg = msg)
            if msg == True:
                con.close() 
                flash("Başarı ile kayıt oldunuz.", "success")
                return redirect(url_for("login"))       
            else:
                flash("Başarısız işlem","warning")
                return redirect(url_for("register"))
    else:
        return render_template("register.html", form = form)
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        with sql.connect("./blog.db") as con:
            cur = con.cursor()
        try:
            username = form.username.data
            password = hashlib.md5(form.password.data.encode()).hexdigest()
            cur.execute("SELECT * from busers where username = ? and password = ?", (username,password))
            rows = cur.fetchone()
            if rows != None:
                flash("Başarıyla giriş yaptınız", "success")
                session["logged_in"] = True
                session["username"] = username
                redirect(url_for("index"))
                # if bcrypt.checkpw(form.password.data.encode('utf8'), rows[4]):
                #     flash(password, "success")
                #     return redirect(url_for("index"))
                # else:
                #     flash("Hatalı parola girdiniz." , "warning")
                #     return redirect(url_for("login"))
            else:
                flash("Kullanıcı adı ya da şifre hatalı", "danger")
                redirect(url_for("login"))
        except sql.IntegrityError as e:
            con.rollback()
            msg = 'sqlite error: ', e.args[0]
            #msg = "error in insert operation"
                  
    return render_template("login.html", form = form)
#Dashboard
@app.route("/dashboard")
@login_required
def dashboard():
        return render_template("dashboard.html")
#Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='127.0.0.1', port=5001)