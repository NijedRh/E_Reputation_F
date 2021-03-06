from src.nlp_fonctions.remove_non_ascii import RemoveNonAscii
from src.nlp_fonctions.to_lowercase import ToLowerCase
from src.nlp_fonctions.remove_ponctuation import RemovePunctuation
from src.nlp_fonctions.replace_number import ReplaceNumber
from src.nlp_fonctions.stop_words import StopWords
from src.nlp_fonctions.replace_contractions import Contractions
from src.nlp_fonctions.lemmatize_verbs import LemmatizeVerbs
import nltk


class CommentCleaning:
    def __init__(self, sample):
        self.sample = sample

    def clean_comment(self):
        cont = Contractions(self.sample)
        sample = cont.replace_contractions()
        # diviser le texte par mot
        words = nltk.word_tokenize(sample)
        non_ascii = RemoveNonAscii(words)
        words = non_ascii.remove_non_ascii()
        lower_case = ToLowerCase(words)
        words = lower_case.to_lowercase()
        punctuation = RemovePunctuation(words)
        words = punctuation.remove_punctuation()
        number = ReplaceNumber(words)
        words = number.replace_numbers()
        stop_words = StopWords(words)
        words = stop_words.remove_stopwords()
        lemma = LemmatizeVerbs(words)
        words = lemma.lemmatize_verbs()

        return words
