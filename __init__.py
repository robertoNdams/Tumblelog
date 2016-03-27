#!/usr/bin/env python3


from flask import Flask

#configure mongoengine  and flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

#Configuration of the tumble_log mongo database 
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

database = MongoEngine(app)

if __name__ == '__main__':
	app.run()
