from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b4d17b47db61ccb90f2cedfed7859bb4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String(20), unique=True, nullable=False)
    email       = db.Column(db.String(120), unique=True, nullable=False)
    image_file  = db.Column(db.String(20), nullable=False, default='default.jpg')
    password    = db.Column(db.String(60), nullable=False)
    post        = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content     = db.Column(db.Text, nullable=False)
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


"""
user_1 = User(username='red', email='red@demo.com', password='password')
user_2 = User(username='blah', email='blah@demo.com', password='password')

db.session.add(user_1)
db.session.add(user_2)
db.session.commit()

QUERYING:
    User.query.all() - get all users
    User.query.first() - get first users

    User.query.filter_by(username='red').all()
    User.query.filter_by(username='red').first()

    User.query.get(1) - get user by id

    user = User.query.get(1)

post_1 = Post(title='article1', 'content'='test1', user_id=user.id)
post_2 = Post(title='article2', 'content'='test2', user_id=user.id)

db.session.add(post_1)
db.session.add(post_2)
db.session.commit()

# delete and create db
    db.drop_all()
    db.create_all()
"""

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        flash('Success bitch!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
