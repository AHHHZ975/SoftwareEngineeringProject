import flask
import bcrypt
from db import mongo


class Signup(flask.views.MethodView):
    def get(self):
        return flask.render_template('sign_up.html')
    
    def post(self):
        required = ['email', 'phoneNumber', 'username', 'password', 'passwordConfirm']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('signup'))
        
        username = flask.request.form['username']
        password = flask.request.form['password']
        passwordConfirm = flask.request.form['passwordConfirm']

        if (username is None):
                flask.flash("This username field is empty!")
                return flask.redirect(flask.url_for('signup'))
        else:       
            users = mongo.db.users
            existingUsers = users.find_one({'username' : flask.request.form['username']})
        
            if existingUsers is None:
                if (passwordConfirm == password):
                    hashpass = bcrypt.hashpw(flask.request.form['password'].encode('utf-8'), bcrypt.gensalt())
                    users.insert({'username' : flask.request.form['username'], 'password' : hashpass})
                    flask.session['username'] = flask.request.form['username']
                    flask.flash("The new account has been created successfully!")
                    return flask.redirect(flask.url_for('login'))
                else:
                     flask.flash("The password and password confirmation are not matched!")
                     return flask.redirect(flask.url_for('signup'))
            else:
                flask.flash("This username already exists in the system!")
                return flask.redirect(flask.url_for('signup'))