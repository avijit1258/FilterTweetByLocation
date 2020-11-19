from gensim import corpora
import gensim
import tweetPreprocessing

def topic_model_lda(texts):
    ''' mine topics using LDA '''
    NUM_TOPICS = 5
    all_tokens = []

    for text in texts:
        tokens = tweetPreprocessing.preprocess_text(text)
        
        all_tokens.append(tokens)

    dictionary = corpora.Dictionary(all_tokens)
    corpus = [dictionary.doc2bow(token) for token in tokens]

    ldamodel = gensim.models.ldamulticore.LdaMulticore(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=12)

    topics = ldamodel.show_topic(0, topn=5)

    # todo process topics from returned format

    return topics