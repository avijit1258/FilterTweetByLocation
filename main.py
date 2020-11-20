import sentimentAnalysis 
import tweetPreprocessing
import topicModeling
import twitterApiConnection

def main():
    # sentimentAnalysis.test_sentiment_polarity_scores()
    # tweetPreprocessing.test_get_lemma()
    # tweetPreprocessing.test_tokenize()
    # tweetPreprocessing.test_preprocess_text()
    # topicModeling.test_topic_model_lda()
    twitterApiConnection.connection()

    return

if __name__ == "__main__":
    main()


