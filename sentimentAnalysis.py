from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tweetPreprocessing
analyzer = SentimentIntensityAnalyzer()

def sentiment_polarity_score(tweets):
    ''' This method returns polarity score for pos, neg, neu and compound '''
    tweets_with_sentiment = {}
    for key, value in tweets.items():
        processed_tweet = ' '.join(tweetPreprocessing.preprocess_text(value))
        snt = analyzer.polarity_scores(processed_tweet)
        tweets_with_sentiment[key] = snt 

    return tweets_with_sentiment

def categorize_tweets_according_to_sentiment(tweets):
    THRESHOLD = 0.6
    tweets_with_sentiment = sentiment_polarity_score(tweets)
    positive = []
    negative = []
    neutral = []

    for key, value in tweets_with_sentiment.items():
        if value['pos'] >= THRESHOLD:
            positive.append(key)
        
        if value['neg'] >= THRESHOLD:
            negative.append(key)

        if value['neu'] >= THRESHOLD:
            neutral.append(key)
        
    return {'pos': positive, 'neg': negative, 'neu': neutral}

def test_sentiment_polarity_scores():

    print('Testing sentiment_polarity_scores')
    texts = ['Academic achievement unlocked: reviewer incorrectly explaining my own prior work to me...',
    'Along with our silicon partners, we’re announcing our new vision for security in Windows to help ensure our customers are protected today – and long into the future.', 'We should just count the atoms at this point', 'Great. My daughter, grandson, and I all have Covid-19. And I have a genetic disorder that weakens my immune response, so it’s going to be a wild ride. Folks: take this shit seriously. It just took a brief visit from my daughter’s ex, to see the baby for a bit, to infect us all.']

    sentiment_polarity_score(texts)
    return

