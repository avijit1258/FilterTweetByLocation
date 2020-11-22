
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


def get_summary_sentiment_category_tweets(sentiment_category_tweets, tweets):

    # print('pos ', len(sentiment_category_tweets['pos']))
    # print('neg ', len(sentiment_category_tweets['neg']))
    # print('neu', len(sentiment_category_tweets['neu']))

    positive_tweets = {key: value for key, value in tweets.items() if key in sentiment_category_tweets['pos']}
    negative_tweets = {key: value for key, value in tweets.items() if key in sentiment_category_tweets['neg']}
    neutral_tweets = {key: value for key, value in tweets.items() if key in sentiment_category_tweets['neu']}

    # print(len(positive_tweets))
    # print(len(negative_tweets))
    # print(len(neutral_tweets))

    positive_summary = summarize_tweets(positive_tweets)
    negative_summary = summarize_tweets(negative_tweets)
    neutral_summary = summarize_tweets(neutral_tweets)


    return {'pos' : positive_summary, 'neg': negative_summary, 'neu': neutral_summary}

def calculate_tweet_sentiment_ratio(tweets_in_category):

    positive_ratio = (len(tweets_in_category['pos']) / 200.0) * 100
    negative_ratio = (len(tweets_in_category['neg']) / 200.0) * 100
    neutral_ratio = (len(tweets_in_category['neu']) / 200.0) * 100

    return {'pos': positive_ratio, 'neg': negative_ratio, 'neu': neutral_ratio}

def summary_sentiment_topic_tweets(keywords):
    TOTAL_TWEETS = 1000
    TWEETS_PER_TOPIC = 200
    topic_tweets = {}
    topic_tweets_summary = {}
    topic_tweets_category = {}
    topic_tweets_category_summary = {}
    topic_tweets_category_ratio = {}
    aggregated_for_frontend = {}

    # get topics from 1000 tweets
    tweets = tAC.searchKeywords(keywords, TOTAL_TWEETS)
    topics = retrive_topics_from_tweets(tweets)

    # get 200 tweets of each topic

    count = 0
    for topic in topics:
        topic_tweets[count] = tAC.searchKeywords(' OR '.join(topic), TWEETS_PER_TOPIC)
        count = count + 1

    # summarizes tweets of a topic
    for key, value in topic_tweets.items():
        topic_tweets_summary[key] = summarize_tweets(value)
        topic_tweets_category[key] = get_tweets_sentiments_with_category(value)
        topic_tweets_category_ratio[key] = calculate_tweet_sentiment_ratio(topic_tweets_category[key])
        
        
    # print('topic_tweets_summary ', topic_tweets_summary)
    # print('topic_tweets_category ', topic_tweets_category)

    for key, value in topic_tweets_category.items():
        topic_tweets_category_summary[key] = get_summary_sentiment_category_tweets(value, topic_tweets[key])

    
    # print('topic_tweets_category_summary ', topic_tweets_category_summary)

    for key, value in topic_tweets.items():
        aggregated_for_frontend[key] = {'title': topic_tweets_summary[key], 'ratio': topic_tweets_category_ratio[key], 'category_summary': topic_tweets_category_summary[key]}
    
    return aggregated_for_frontend


    
    

    

    

    

