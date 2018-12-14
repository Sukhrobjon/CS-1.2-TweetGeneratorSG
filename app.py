from flask import Flask
from markov_chain import make_sentence_with_markov
app = Flask(__name__)


@app.route('/')
def hello_world():
    return make_sentence_with_markov(15)

if __name__ == '__main__':
    app.run(debug=True)


