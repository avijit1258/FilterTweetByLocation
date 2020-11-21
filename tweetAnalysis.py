
import tweetSummarization
import topicModeling
import sentimentAnalysis

def get_tweets_sentiments(tweets):

    return sentimentAnalysis.sentiment_polarity_score(tweets)

def summarize_tweets(tweets):

    return tweetSummarization.text_summarize(tweets)

def retrive_topics_from_tweets(tweets):
    
    return topicModeling.topic_model_lda(list(tweets.values()))