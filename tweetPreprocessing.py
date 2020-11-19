from spacy.lang.en import English
import nltk
from nltk.corpus import wordnet 

def preprocess_text(text):
    nltk.download('stopwords')
    en_stop = set(nltk.corpus.stopwords.words('english'))

    tokens = tokenize(text)
    # print(tokens)
    tokens = [token for token in tokens if len(token) >= 2]
    # print(tokens)
    tokens = [token for token in tokens if token not in en_stop]
    # print(tokens)
    tokens = [ get_lemma(token) for token in tokens] 
    # print(tokens)
    return tokens


def tokenize( text):
    ''' Tokenize a word. '''
    parser = English()
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

