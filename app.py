import flask, flask.views
import settings

# import views
from login import Login
from remote import Remote
from music import Music
from main import Main
from contact import Contact
from about import About

app = flask.Flask(__name__)
app.secret_key = settings.secret_key


# Directories
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=["GET", "POST"])

app.add_url_rule('/about',
                 view_func=About.as_view('about'),
                 methods=["GET", "POST"])

app.add_url_rule('/contact',
                 view_func=Contact.as_view('contact'),
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


@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404

app.debug = True
app.run()
 