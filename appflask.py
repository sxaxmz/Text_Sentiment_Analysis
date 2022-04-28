from flask import Flask, request, redirect, url_for, render_template
from code_NLTK import analyze

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('text_sentiment_analysis'))

@app.route("/text_sentiment_analysis", methods=['POST','GET'])    
def homepage():
    if request.method == 'POST':
        textarea = request.form['text_input']
        sen = analyze(textarea)
    return render_template('main.html', title='Text Sentiment Analysis', sentiment=sen)

if __name__ == '__main__':
    #app.debug = True
    app.run(host='127.0.0.1', port=5000)