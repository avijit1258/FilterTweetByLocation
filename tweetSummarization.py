from gensim.summarization.summarizer import summarize
from gensim.summarization.textcleaner import clean_text_by_sentences as _clean_text_by_sentences
from gensim.summarization.textcleaner import get_sentences
import tweetPreprocessing as tp

# To Do
# Use gensim summarization to summarize tweets

tweets = ['Our proposal for a digital contact tracing system #PanCast  that goes beyond smartphone-based solutions. It''s a joint collaboration with Gilles Barthe, @rdeviti, Peter Druschel, Deepak Garg,  @autreche, Pierfrancesco Ingo, @mattlentz_ & @bschoelkopf. http://pancast.mpi-sws.org', 'Sending good vibes to everyone fighting to make it through BFCM','I really dropped all my hobbies and talents in order to focus on ‘productivity’ and chasing the bag in college damn']

def get_sentences_from_text(text):
    ''' returns generator of texts '''

    return get_sentences(text)


def text_summarize(texts):
    summary = summarize(texts)
    print('summary ', summary)
    return summary

def prepare_tweet(tweet):
    processed_tweet = []
    for line in get_sentences(tweet):
        processed_tweet.append(' '.join(tp.preprocess_text(line)) )

    return '.'.join(processed_tweet)

def test_prepare_tweet_for_summary_and_sentiment():
    for tweet in tweets:
        print(prepare_tweet_for_summary_and_sentiment)
    return

def test_text_summarize():
    print('...Testing tokenize....')
    
    # print(str(tweets))
    # print(text_summarize(tweets[0]))
    for tweet in tweets:
        # print(clean_text_by_sentences(tweet))
        print([e for e in get_sentences(tweet) ])
    
    return
