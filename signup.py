import flask

users = {'AHZ':'123'}

class Signup(flask.views.MethodView):
    def get(self):
        return flask.render_template('sign_up.html')
    
    def post(self):
        # if 'logout' in flask.request.form:
        #     flask.session.pop('username', None)
        #     return flask.redirect(flask.url_for('login'))
        required = ['email', 'phoneNumber', 'username', 'password', 'passwordConfirm']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('signup'))
        
        username = flask.request.form['username']
        password = flask.request.form['password']
        passwordConfirm = flask.request.form['passwordConfirm']

        if (username is ''):
                flask.flash("This username field is empty!")
                return flask.redirect(flask.url_for('signup'))
        else:       
            if (username not in users):
                if (passwordConfirm == password):
                    email = flask.request.form['email']
                    phoneNumber = flask.request.form['phoneNumber']
                    flask.flash("The new account has been created successfully!")
                    return flask.redirect(flask.url_for('login'))
                else:
                     flask.flash("The password and password confirmation are not matched!")
                     return flask.redirect(flask.url_for('signup'))
            else:
                flask.flash("This username already exists in the system!")
                return flask.redirect(flask.url_for('signup'))
        
        
