import flask, flask.views
from flask import app


# import views
from signup import Signup
from login import Login
from search import Search
from music import Music
from main import Main
from contact import Contact
from about import About
from db import app

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

app.add_url_rule('/signup',
                 view_func=Signup.as_view('signup'),
                 methods=["GET", "POST"])

app.add_url_rule('/search/',
                 view_func=Search.as_view('search'),
                 methods=['GET', 'POST'])
                 
app.add_url_rule('/music/',
                 view_func=Music.as_view('music'),
                 methods=['GET', 'POST'])


@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404

app.debug = True
app.run()
 