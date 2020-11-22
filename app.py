from flask import Flask
from flask import request
from flask import render_template
import tweetAnalysis

app = Flask('app')


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return "Hello World"
    else:
        return render_template('home.html')

@app.route('/get_topic_summary', methods=['GET', 'POST'])
def topics_with_sentiment_summary():
    return tweetAnalysis.summary_sentiment_topic_tweets('health')

app.run(host='0.0.0.0', port=8080)
