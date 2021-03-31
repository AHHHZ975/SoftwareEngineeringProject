import flask
from utils import login_required
import os

class Music(flask.views.MethodView):
    @login_required
    def get(self):
        songs = os.listdir('C:/Users/AmirHossein/OneDrive/Desktop/flask-tutorial-master/flask-tutorial-master/part 4 - music/static/music')
        return flask.render_template("music.html", songs=songs)
    
    @login_required
    def post(self):
        return flask.render_template("music.html")
