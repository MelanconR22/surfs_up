#import dependencies
from flask import Flask

#create instance
app = Flask(__name__)

#create flask route
@app.route('/')

#create function called hello_world()
@app.route('/')
def hello_world():
    return 'Hello world, what are you doing?'