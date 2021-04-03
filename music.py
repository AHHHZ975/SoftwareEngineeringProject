import flask
from utils import login_required
import os
from search import Search

class Music(flask.views.MethodView):
    @login_required
    def get(self):        
        songs = os.listdir('./static/music')
        return flask.render_template("music.html", songs=songs)
    
    @login_required
    def post(self):
        searchText = flask.request.form['search']
        Search.getMusic(Search, searchText)
        Search.getMusicInformation(Search, searchText)
        return flask.redirect(flask.url_for('music'))
