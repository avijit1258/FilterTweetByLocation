import sentimentAnalysis 
import tweetPreprocessing
import topicModeling
import twitterApiConnection
import tweetSummarization

def main():
    # sentimentAnalysis.test_sentiment_polarity_scores()
    # tweetPreprocessing.test_get_lemma()
    # tweetPreprocessing.test_tokenize()
    # tweetPreprocessing.test_preprocess_text()
    # print(twitterApiConnection.retrive_topics_from_tweets())
    # print(twitterApiConnection.summarize_tweets())
    # twitterApiConnection.connection()
    # tweetSummarization.test_text_summarize()
    #tweetSummarization.test_prepare_tweet_for_for_analysis()
    # print(twitterApiConnection.summarize_tweets())
    print(tweetPreprocessing.test_get_synonyms_of_word())
    
    return

if __name__ == "__main__":
    main()


