from flask import Flask, request, url_for, redirect
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app)

class CreateForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=64)])
    email = StringField('Email Address', [validators.Length(min=6, max=254)])
    password = PasswordField('New Password', [validators.Length(min=6, max=64)])

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(254), nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<User %r>' % (self.username)

@app.route('/')
def index():
    create_url = url_for('create')
    users = User.query.all()
    return render_template('index.html',
                           title='Secret',
                           users=users,
                           create_url=create_url)

@app.route('/create/', methods=['GET', 'POST'])
def create():
    form = CreateForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        # return redirec(turl_for('index'))
    return render_template('create.html', form=form)

if __name__ == "__main__":
    app.run()