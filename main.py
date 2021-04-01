import flask, flask.views
import os

class Main(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')

    def post(self):
        if self.form['login_button'] == 'Login':
            return flask.render_template('login.html')
        elif self.form['signup_button'] == 'SignUp':
            return flask.render_template('sign_up.html')

