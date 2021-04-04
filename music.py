import flask
from utils import login_required
import os
from search import Search
import json
from db import mongo

class Music(flask.views.MethodView):
    @login_required
    def get(self):        
        # songs = os.listdir('./static/music')
        # Display the user's search history
        users = mongo.db.users
        currentUser = users.find_one({'username' :  flask.session['username']})
        songs = []
        for searchHistory in currentUser['searchHistory']:
            songs.append(searchHistory['title'])

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
        if  len(musicInformation):
            artist = musicInformation[0]['artist']
            title = musicInformation[0]['title']
            time = musicInformation[0]['time']
            downloadLink = musicInformation[0]['download_link']
        else:
            artist = ''
            title = ''
            time = ''
            downloadLink = ''
        
        if len(musicLyric):
            lyric = musicLyric[0]['lyric']
        else:
            lyric = ''
        
        # download the music
        # r = requests.get(downloadLink, allow_redirects=True)
        # open(f'./static/music/{title}.mp3', 'wb').write(r.content)
        
        # songs = os.listdir('./static/music')
        if artist and title and time and downloadLink and lyric:
            # update user database with his/her search history
            users = mongo.db.users
            searchedMusic = {   "title": title,
                                "artist": artist,
                                "downloadLink": downloadLink,
                                "time": time,
                                "lyric": lyric 
                            }
            users.update({'username': flask.session['username']}, {'$push': {'searchHistory': searchedMusic}})
            

            currentUser = users.find_one({'username' :  flask.session['username']})            
            # for searchHisrory in currentUser['searchHistory']:
            #     if searchHistory['title']            
            songs = []
            for searchHistory in currentUser['searchHistory']:
                songs.append(searchHistory['title'])
            return flask.render_template("music.html", lyric=lyric, artist=artist, title=title, time=time, downloadLink=downloadLink, songs=songs)
        else:
            flask.flash('Sorry, the music not found!')          
            return flask.redirect(flask.url_for('music'))
