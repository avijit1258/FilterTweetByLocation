from flask import Flask
from flask import request
from flask import render_template
import tweetAnalysis

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return "Hello World"
    else:
        return render_template('home.html')

@app.route('/get_topic_summary', methods=['GET', 'POST'])
def topics_with_sentiment_summary():
    tweet_data = tweetAnalysis.summary_sentiment_topic_tweets('health')
    return render_template('home_data.html', tweet_data = tweet_data)

app.run(host='0.0.0.0', port=8080)
