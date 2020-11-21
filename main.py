
import twitterApiConnection
import tweetAnalysis

def main():
   
    tweets = twitterApiConnection.searchKeywords("covid", count = 100)

    print(tweetAnalysis.retrive_topics_from_tweets(tweets))
    # print(tweetAnalysis.summarize_tweets(tweets))
    # print(tweetAnalysis.get_tweets_sentiments(tweets))

    
    return

if __name__ == "__main__":
    main()


