import json
from src.driver_actions.extract_comment import CommentExtractor
from src.driver_actions.extract_text import TextExtractor
from src.driver_actions.extract_reaction import ReactExtractor
from src.sentiment_analyszer.sentiment import SentimentAnalyzer
class SavingData :
    def __init__(self,  list_web_element):
        self.list_web_element = list_web_element

    def save_data (self):
        data = dict()
        k = 1
        for web_element in self.list_web_element:
            #fonction retourne la description du poste
            text = TextExtractor(web_element)
            #fonction retourne les commentaires
            comment = CommentExtractor(web_element)
            #fonction retourne nombre de réaction
            react = ReactExtractor(web_element)
            data["post_num_" + str(k)] = dict()
            data["post_num_" + str(k)]['titre'] = text.extract_text()
            data["post_num_" + str(k)]['react'] = react.extract_react
            data["post_num_" + str(k)]['commentaires'] = comment.extract_comment()

            k = k + 1
        comments = CommentExtractor(self.list_web_element)
        #pnn =SentimentAnalyzer(self.list_web_element)
        data["nombre de commentaire totales" ]= comments.extract_nbr_comment()
        """data["nombre de commentaire positive "]=comments.extract_comment()
        data["nombre de commentaire negative "]=comments.extract_comment()
        data["nombre de commentaire neutre "]= comments.extract_comment()"""

        with open('profile_posts_data.json', 'w', encoding='utf-8') as json_file:
         json.dump(data, json_file, ensure_ascii=False, indent=1 , separators= (',', ':'))
