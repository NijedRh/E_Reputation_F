from nltk.stem import LancasterStemmer
class StemWords :
    def __init__(self, words):
        self.words = words

    def stem_words(self):
        #Stem words dans la liste des mots tokenisés
        stemmer = LancasterStemmer()
        stems = []
        for word in self.words:
            stem = stemmer.stem(word)
            stems.append(stem)
        return stems