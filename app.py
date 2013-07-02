from flask import Flask, render_template
from random import choice
## Helpers
def get_word():
    words = [
            "potato",
            "the",
            "it",
            "Bruce"
            ]
    return choice(words)
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html', word=get_word())

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/results/')
def results():
    return render_template('results.html')

@app.route('/feedback/')
def feedback():
    return render_template('feedback.html')

if __name__ == "__main__":
    app.run(debug=True)
