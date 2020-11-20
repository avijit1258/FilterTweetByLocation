from spacy.lang.en import English
import nltk
from nltk.corpus import wordnet 

nltk.download('wordnet')
nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))
parser = English()

tweets = ['Our proposal for a digital contact tracing system #PanCast  that goes beyond smartphone-based solutions. It''s a joint collaboration with Gilles Barthe, @rdeviti, Peter Druschel, Deepak Garg,  @autreche, Pierfrancesco Ingo, @mattlentz_ & @bschoelkopf. http://pancast.mpi-sws.org', 'Sending good vibes to everyone fighting to make it through BFCM','I really dropped all my hobbies and talents in order to focus on ‘productivity’ and chasing the bag in college damn']


def get_synonyms_of_word(word):
    synonyms = wordnet.synsets(word)

    return synonyms

def test_get_synonyms_of_word():
    words = ['health', 'covid', 'vaccine', 'pandemic']

    for word in words:
        print(word, ' ', get_synonyms_of_word(word))

    return

def preprocess_text(text):
    
    tokens = tokenize(text)
    # print(tokens)
    tokens = [token for token in tokens if len(token) > 2]
    # print(tokens)
    tokens = [token for token in tokens if token not in en_stop]
    # print(tokens)
    tokens = [ get_lemma(token) for token in tokens] 
    # print(tokens)
    return tokens


def tokenize( text):
    ''' Tokenize a word. '''
    
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens

def test_tokenize():
    print('...Testing tokenize....')
    

    for tweet in tweets:
        print(tweet)
        print(tokenize(tweet))
    return

def test_preprocess_text():
    print('...testing preprocess_text....')

    for tweet in tweets:
        print(tweet)
        print(preprocess_text(tweet))

    return


def get_lemma(word):
    ''' Returns lemma of a word '''
    lemma = wordnet.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma

def test_get_lemma():
    words = ['eating', 'having', 'drove', 'fall', 'fallen']

    for word in words:
      print(word, ' ',get_lemma(word))
    
    return

