from flask import flash, redirect, render_template, request, session
from login_registration_app import app,bcrypt
from login_registration_app.models.users_model import User


@app.route("/" , methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/register",methods=['POST'])
def registration():
    if not User.validate_registration(request.form):
            return redirect("/")
        
    password_encriptado = bcrypt.generate_password_hash(request.form['password1'])
    data = {
        'first_name':request.form['firstname'],
        'last_name':request.form['lastname'],
        'email':request.form['email'],
        'password':password_encriptado
    }
    response_query = User.create_user(data)
    print(response_query)
    session['name'] = request.form['firstname']
    return redirect("/result")

@app.route("/login",methods=['POST'])
def login():
    response_query_user=User.validate_login(request.form)
    
    if not response_query_user['is_valid']:
        return redirect("/")
    
    if not bcrypt.check_password_hash( response_query_user['user']['password'], request.form['password']):
        flash("el password no es correcto","login")
        return redirect("/")
    session['name'] = response_query_user['user']['first_name']
    return redirect("/result")

@app.route("/result",methods=['GET'])
def result_user():
    return render_template("result.html")
