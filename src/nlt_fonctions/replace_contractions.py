import contractions
class Contractions:
    def __init__(self , sample):
        self.sample =sample
    def replace_contractions(self):
        #Remplacer les contractions dans la chaîne de texte
        return contractions.fix(self.sample)