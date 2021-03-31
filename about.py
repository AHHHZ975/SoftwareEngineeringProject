import flask, flask.views

class About(flask.views.MethodView):
    def get(self):
            return flask.render_template('about.html')
    def post(self):
        pass