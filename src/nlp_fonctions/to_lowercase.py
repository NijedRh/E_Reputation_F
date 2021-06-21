class ToLowerCase :
    def __init__(self,words):
        self.words =words

    def to_lowercase(self):
        #Convertir tous les caractères en minuscules
        new_words = []
        for word in self.words:
            new_word = word.lower()
            new_words.append(new_word)
        return new_words