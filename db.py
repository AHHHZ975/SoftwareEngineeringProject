import flask
import settings
from flask_pymongo import PyMongo


app = flask.Flask(__name__)
app.secret_key = settings.secret_key
app.config['MONGO_DBNAME'] = 'mongologinexample'
app.config['MONGO_URI'] = 'mongodb+srv://ahz:123@cluster0.gu31r.mongodb.net/MusicCloud?retryWrites=true&w=majority'

mongo = PyMongo(app)
