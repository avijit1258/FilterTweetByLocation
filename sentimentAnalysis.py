from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def sentiment_polarity_score(tweets):
    ''' This method returns polarity score for pos, neg, neu and compound '''
    tweets_with_sentiment = {}
    for key, value in tweets.items():
        snt = analyzer.polarity_scores(value)
        tweets_with_sentiment[key] = snt 

    return tweets_with_sentiment

def test_sentiment_polarity_scores():

    print('Testing sentiment_polarity_scores')
    texts = ['Academic achievement unlocked: reviewer incorrectly explaining my own prior work to me...',
    'Along with our silicon partners, we’re announcing our new vision for security in Windows to help ensure our customers are protected today – and long into the future.', 'We should just count the atoms at this point', 'Great. My daughter, grandson, and I all have Covid-19. And I have a genetic disorder that weakens my immune response, so it’s going to be a wild ride. Folks: take this shit seriously. It just took a brief visit from my daughter’s ex, to see the baby for a bit, to infect us all.']

    sentiment_polarity_score(texts)
    return

