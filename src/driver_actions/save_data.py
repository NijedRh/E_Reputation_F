import json
from src.driver_actions.extract_comment import CommentExtractor
from src.driver_actions.extract_text import TextExtractor
from src.driver_actions.extract_reaction import ReactExtractor
from src.sql_database.db import Db ,DB2
class SavingData :
    def __init__(self,  list_web_element):
        self.list_web_element = list_web_element

    def save_data (self):
        data = dict()
        k = 1
        for web_element in self.list_web_element:
            text = TextExtractor(web_element)
            comment = CommentExtractor(web_element)
            react = ReactExtractor(web_element)
            data["post_num_" + str(k)] = dict()
            data["post_num_" + str(k)]['titre'] = text.extract_text()
            data["post_num_" + str(k)]['react']=dict()
            data["post_num_" + str(k)]['react']['J’aime '] = react.extract_react[0]
            data["post_num_" + str(k)]['react']['J’adore ' ] = react.extract_react[1]
            data["post_num_" + str(k)]['react']['Haha'] = react.extract_react[2]
            data["post_num_" + str(k)]['react']['Grrr' ] = react.extract_react[3]
            data["post_num_" + str(k)]['commentaires']=dict()
            data["post_num_" + str(k)]['commentaires']  = comment.extract_comment()
            #data["post_num_" + str(k)]['post_sent'] =react.extract_react()
            insertion = Db(k, data["post_num_" + str(k)]['titre'],
                           data["post_num_" + str(k)]['react']['J’aime '],data["post_num_" + str(k)]['react']['J’adore ' ],data["post_num_" + str(k)]['react']['Haha'], data["post_num_" + str(k)]['react']['Grrr' ],data["post_num_" + str(k)]['commentaires']
                           )
            insertion.connect()

            k = k + 1
        comments = CommentExtractor(self.list_web_element)
        data["nombre de commentaire totales" ]= comments.extract_nbr_comment()
        insertion2=DB2(data["nombre de commentaire totales" ])
        insertion2.connect2()
        """data["nombre de commentaire positive "]=comments.extract_comment()
        data["nombre de commentaire negative "]=comments.extract_comment()
        data["nombre de commentaire neutre "]= comments.extract_comment()"""

        with open('profile_posts_data.json', 'w', encoding='utf-8') as json_file:
         json.dump(data, json_file, ensure_ascii=False, indent=1 , separators= (',', ':'))

