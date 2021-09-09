from flask import Flask
from flask-mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'birthdaybot',
    'host': 'localhost',
    'port': 

}

