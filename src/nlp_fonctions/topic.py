from gensim import corpora , models
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
class Topics :

    def topic_model(self , sample):
       a=keywords(sample, words=1)
       return  str(a)
    def lda_model(self , sample):
        dictionary = corpora.Dictionary([sample])
        corpus = [dictionary.doc2bow(text.split()) for text in sample]
        lda_model = models.ldamodel.LdaModel(corpus,num_topics=2,id2word=dictionary)

        return str(lda_model.print_topics())


