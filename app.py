from flask import Flask, render_template
from markov_chain import make_sentence_with_markov

app = Flask(__name__)


@app.route('/')
def create_sentence():
    sentence = make_sentence_with_markov(15)
    return render_template("index.html", sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True)


