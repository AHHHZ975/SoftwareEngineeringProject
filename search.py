import flask
from utils import login_required

class Search(flask.views.MethodView):
    @login_required
    def get(self):
        return flask.render_template('search.html')
        
    @login_required
    def post(self):
        searchText = flask.request.form['expression']
        # flask.flash(searchText)
        return flask.redirect(flask.url_for('search'))
