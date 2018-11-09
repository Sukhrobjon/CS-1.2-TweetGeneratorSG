from flask import Flask
from random_sentence import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return make_random_sentence(10)

if __name__ == '__main__':
    app.run()