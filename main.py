import flask, flask.views
from flask.globals import session
from db import mongo

class Main(flask.views.MethodView):
    def get(self):
        statistics = mongo.db.statistics

        # Known user
        if 'username' in session:
            existingUser = statistics.find_one({'username' : flask.session['username']})                
            if existingUser:
                view = existingUser['view']
                statistics.update_one({'username': flask.session['username']}, {'$set': {'view': view + 1}}, upsert=False)
                view += 1
            else:
                statistics.insert({'username' : flask.session['username'], 'view' : 1})
                view = 1
        # Anonymous user        
        else:
            view = statistics.find_one({'username' : 'anonymous'})['view']
            statistics.update_one({'username': 'anonymous'}, {'$set': {'view': view + 1}}, upsert=False)
            view += 1

        # Total visiting number
        totalVisitingNumber = 0
        for statistic in statistics.find():    
            totalVisitingNumber += statistic['view']

        return flask.render_template('index.html', totalVisitingNumber=totalVisitingNumber, userVisitingNumber=view)

    def post(self):
        if self.form['login_button'] == 'Login':
            return flask.render_template('login.html')
        elif self.form['signup_button'] == 'SignUp':
            return flask.render_template('sign_up.html')

