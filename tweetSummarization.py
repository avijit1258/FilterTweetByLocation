from gensim.summarization.summarizer import summarize
from gensim.summarization.textcleaner import clean_text_by_sentences as _clean_text_by_sentences
from gensim.summarization.textcleaner import get_sentences


# To Do
# Use gensim summarization to summarize tweets

def clean_text_by_sentences(text):

    return _clean_text_by_sentences(text)

def get_sentences_from_text(text):

    return get_sentences(text)

def text_summarize(texts):

    return summarize(texts)

def test_all