import flask, flask.views

class Contact(flask.views.MethodView):
    def get(self):
            return flask.render_template('contact.html')
    def post(self):
        pass