import unicodedata
class RemoveNonAscii :
    def __init__(self , words):
        self.words = words

    def remove_non_ascii(self):
        #Supprimer les caractères non ASCII de la liste des mots tokenisés
        new_words = []
        for word in self.words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
        return new_words