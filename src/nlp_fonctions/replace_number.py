import inflect
class ReplaceNumber :
    def __init__(self, words):
        self.words = words

    def replace_numbers(self):
        #Remplacer toutes les occurrences d'entier dans la liste des mots tokenisés par une représentation textuelle
        p = inflect.engine()
        new_words = []
        for word in self.words:
            if word.isdigit():
                new_word = p.number_to_words(word)
                new_words.append(new_word)
            else:
                new_words.append(word)
        return new_words