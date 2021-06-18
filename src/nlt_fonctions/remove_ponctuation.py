import re
class RemovePunctuation:
    def __init__(self, words):
        self.words= words

    def remove_punctuation(self):
        #Supprimer la ponctuation de la liste des mots tokenisés
        new_words = []
        for word in self.words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
        return new_words
