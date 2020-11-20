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
    print(topicModeling.topic_model_lda(twitterApiConnection.searchKeywords("heart attack",10000)))
    # twitterApiConnection.connection()
    # tweetSummarization.test_text_summarize()
    return

if __name__ == "__main__":
    main()


