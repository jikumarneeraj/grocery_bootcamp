from flask import Flask, render_template,request,redirect,url_for,flash
from app import app
from models import db,User,Product,Category,Cart,Transaction,Order
from werkzeug.security import generate_password_hash,check_password_hash
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username=request.form.get('username')
    password=request.form.get('password')

    if not username or not password:
        flash('Please fill out all fields')
        return redirect(url_for('login'))

    user=User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.passhash,password):
        flash('Invalid username or password')
        return redirect(url_for('login'))

    return redirect(url_for('index'))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register',methods=['POST'])
def register_post():
    username=request.form.get('username')
    password=request.form.get('password')
    confirm_password=request.form.get('confirm_password')
    name= request.form.get('name')
    
    if not username or not password or not confirm_password:
        flash('Please fill out all field')
        return render_template('register.html')
    
    if password != confirm_password:
        flash('Passwords do not match')
        return redirect(url_for('register'))
    
    user=User.query.filter_by(username=username).first()

    if user:
        flash('Username already exists')
        return redirect(url_for('register'))
    
    password_hash=generate_password_hash(password)

    new_user=User(username=username, passhash=password_hash, name=name)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))