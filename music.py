import flask
from utils import login_required
import os
from search import Search
import json
import requests

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

        with open('./db/sounds.json') as f:
            musicInformation = json.load(f) 

        with open('./db/lyrics.json') as f:
            musicLyric = json.load(f)             
        
        # Music information
        artist = musicInformation[0]['artist']
        title = musicInformation[0]['title']
        time = musicInformation[0]['time']
        downloadLink = musicInformation[0]['download_link']
        lyric = musicLyric[0]['lyric']

        # download the music
        r = requests.get(downloadLink, allow_redirects=True)
        open(f'./static/music/{title}.mp3', 'wb').write(r.content)
        songs = os.listdir('./static/music')
        return flask.render_template("music.html", songs=songs, lyric=lyric, artist=artist, title=title, time=time, downloadLink=downloadLink)
        # return flask.redirect(flask.url_for('music'))
