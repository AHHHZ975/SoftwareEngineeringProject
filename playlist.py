import flask, flask.views
from utils import login_required
from bestsong import BestSong
from search import Search
import json
from db import mongo

class Playlist(flask.views.MethodView):
    @login_required
    def get(self):     
        users = mongo.db.users
        currentUser = users.find_one({'username' :  flask.session['username']})
        songs = []
        for playlist in currentUser['playlist']:
            songs.append(playlist['title'])

        return flask.render_template("playlist.html", songs=songs)
    
    @login_required
    def post(self): 
        # Suggest best songs
        bestTitles = BestSong.getBetsSongTitle()


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
        if True: #artist and title and time and downloadLink and lyric:                

            # update user database with his/her search history
            users = mongo.db.users
            musics = mongo.db.musics
            searchedMusic = {   "title": title,
                                "artist": artist,
                                "downloadLink": downloadLink,
                                "time": time,
                                "lyric": lyric
                            }                        
            users.update({'username': flask.session['username']}, {'$push': {'searchHistory': searchedMusic}})
                        

            # view of the music                
            existingMusics = musics.find_one({'title' : title})                
            if existingMusics is None:
                musics.insert({'title' : title, 'artist' : artist, 'downloadLink' : downloadLink, 'time': time, 'view': 1})
            else:
                view = existingMusics['view']
                musics.update_one({'title': title}, {'$set': {'view': view + 1}}, upsert=False)

            
            currentUser = users.find_one({'username' :  flask.session['username']})            
            # for searchHisrory in currentUser['searchHistory']:
            #     if searchHistory['title']
                        


            # Search history of the current user             
            songs = []
            for searchHistory in currentUser['searchHistory']:
                songs.append(searchHistory['title'])
            return flask.render_template("playlist.html", lyric=lyric, artist=artist, title=title, time=time, downloadLink=downloadLink, songs=songs, bestSongs=bestTitles)
        else:
            flask.flash('Sorry, the music not found!')          
            return flask.redirect(flask.url_for('playlist'))

        