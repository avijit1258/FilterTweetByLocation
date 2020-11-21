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


def text_summarize(tweets):
    # print('passage: ', merge_tweets_as_passage(tweets))
    summary = summarize(merge_tweets_as_passage(tweets), word_count = 200)
    # print('summary ', summary)
    return summary

def prepare_tweet_for_analysis(tweet):
    processed_tweet = []
    for line in get_sentences(tweet):
        processed_tweet.append(' '.join(tp.preprocess_text(line)) )
        
    return '.'.join(processed_tweet)

def merge_tweets_as_passage(tweets):
    # print(tweets)
    for key,value in tweets.items():
        tweets[key] = prepare_tweet_for_analysis(value)

    return ' '.join(list(tweets.values()))

def test_prepare_tweet_for_for_analysis():
    print('...Testing prepare tweet....')
    for tweet in tweets:
        print(prepare_tweet_for_analysis(tweet))
    return

def test_text_summarize():
    print('...Testing tokenize....')
    
    return
