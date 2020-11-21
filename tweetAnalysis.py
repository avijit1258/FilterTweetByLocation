
import tweetSummarization
import topicModeling
import sentimentAnalysis
import twitterApiConnection as tAC

def get_tweets_sentiments_with_category(tweets):

    return sentimentAnalysis.categorize_tweets_according_to_sentiment(tweets)

def summarize_tweets(tweets):

    return tweetSummarization.text_summarize(tweets)

def retrive_topics_from_tweets(tweets):
    
    return topicModeling.topic_model_lda(list(tweets.values()))

def summary_sentiment_topic_tweets():
    TOTAL_TWEETS = 1000
    TWEETS_PER_TOPIC = 200

    # get topics from 1000 tweets
    tweets = tAC.searchKeywords("health", TOTAL_TWEETS)
    topics = retrive_topics_from_tweets(tweets)

    # get 200 tweets of each topic
    topic_tweets = {}
    topic_tweets_summary = {}
    topic_tweets_category = {}

    count = 0
    for topic in topics:
        topic_tweets[count] = tAC.searchKeywords(' OR '.join(topic), TWEETS_PER_TOPIC)
        count = count + 1

    # summarizes tweets of a topic
    for key, value in topic_tweets.items():
        topic_tweets_summary[key] = summarize_tweets(value)
        topic_tweets_category[key] = get_tweets_sentiments_with_category(value)

    print('topic_tweets_summary ', topic_tweets_summary)
    print('topic_tweets_category ', topic_tweets_category)

        # print('Topic ', key, ' ',summarize_tweets(value))

    
    

    

    

    

