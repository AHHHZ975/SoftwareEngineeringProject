import flask
from db import mongo
import bcrypt


class Login(flask.views.MethodView):
    def get(self):
        return flask.render_template('login.html')
    
    def post(self):
        if 'logout' in flask.request.form:
            flask.session.pop('username', None)
            return flask.redirect(flask.url_for('login'))
        required = ['username', 'password']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('login'))
        
        username = flask.request.form['username']
        password = flask.request.form['password']
        
        
        if (username is None):
                flask.flash("This username field is empty!")
                return flask.redirect(flask.url_for('login'))
        else:       
            users = mongo.db.users
            logInUser = users.find_one({'username' : flask.request.form['username']})

            if logInUser:                
                if bcrypt.hashpw(flask.request.form['password'].encode('utf-8'), logInUser['password'].encode('utf-8')) == logInUser['password'].encode('utf-8').decode():
                    flask.session['username'] = flask.request.form['username']                    
                    return flask.redirect(flask.url_for('login'))
                else:
                     flask.flash("The password is not correct!")
                     return flask.redirect(flask.url_for('login'))
            else:
                flask.flash("This username doesn't exists in the database!")
                return flask.redirect(flask.url_for('login'))