from nltk.stem import WordNetLemmatizer

class LemmatizeVerbs :
    def __init__(self, words):
        self.words =words

    def lemmatize_verbs(self):
        #Lemmatiser les verbes dans une liste des mots tokenisés
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for word in self.words:
            lemma = lemmatizer.lemmatize(word, pos='v')
            lemmas.append(lemma)
        return lemmas