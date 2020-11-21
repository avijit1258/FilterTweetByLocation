
import twitterApiConnection
import tweetAnalysis

def main():
   
    # tweets = twitterApiConnection.searchKeywords("covid")

    # print(tweetAnalysis.retrive_topics_from_tweets(tweets))
    # print(tweetAnalysis.summarize_tweets(tweets))
    # print(tweetAnalysis.get_tweets_sentiments(tweets))
    tweetAnalysis.summary_sentiment_topic_tweets()

    
    return

if __name__ == "__main__":
    main()


