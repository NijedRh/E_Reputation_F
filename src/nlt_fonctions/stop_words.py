from nltk.corpus import stopwords
class StopWords :
    def __init__(self, words):
        self.words =words

    def remove_stopwords(self):
        #Supprimer stop words de la liste des mots tokenisés
        new_words = []
        for word in self.words:
            if word not in stopwords.words('english'):
                new_words.append(word)
        return new_words