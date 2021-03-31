import flask
import settings

# import views
from login import Login
from remote import Remote
from music import Music
from main import Main

app = flask.Flask(__name__)
app.secret_key = settings.secret_key


# Directories
app.add_url_rule('/',
                 view_func=Main.as_view('index'),
                 methods=["GET", "POST"])
    
app.add_url_rule('/login',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])
app.add_url_rule('/remote/',
                 view_func=Remote.as_view('remote'),
                 methods=['GET', 'POST'])
app.add_url_rule('/music/',
                 view_func=Music.as_view('music'),
                 methods=['GET'])


app.debug = True
app.run()
 