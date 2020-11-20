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
    # topicModeling.test_topic_model_lda()
    # twitterApiConnection.connection()
    # tweetSummarization.test_text_summarize()
    twitterApiConnection.searchKeywords("covid",5)
    return

if __name__ == "__main__":
    main()


