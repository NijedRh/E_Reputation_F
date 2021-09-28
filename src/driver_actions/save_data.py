import json
from src.driver_actions.extract_comment import CommentExtractor
from src.driver_actions.extract_text import TextExtractor
from src.driver_actions.extract_reaction import ReactExtractor
from src.sentiment_analyszer.sentiment_post import SentimentPost
from src.driver_actions.extract_date import DateExtractor
# from src.sql_database.db import Db ,DB2
# from src.sql_database.dddbb import Db3
# import pandas as pd
class SavingData:
    def __init__(self, list_web_element):
        self.list_web_element = list_web_element

    def save_data(self):
        data = dict()
        k = 1
        lp = []
        lneg = []
        lneu = []
        l_reaction = []
        for web_element in self.list_web_element:
            text = TextExtractor(web_element).extract_text()
            comment = CommentExtractor(web_element).extract_comment()
            react = ReactExtractor(web_element).extract_react
            date = DateExtractor(web_element).extract_date()
            data["post" + str(k)] = dict()
            data["post" + str(k)]['titre'] = text[0]
            data["post" + str(k)]['date'] = date
            data["post" + str(k)]['topic'] = text[1]
            data["post" + str(k)]['react'] = dict()
            data["post" + str(k)]['react']['J’aime '] = react[0]
            data["post" + str(k)]['react']['J’adore '] = react[1]
            data["post" + str(k)]['react']['Haha'] = react[2]
            data["post" + str(k)]['react']['Grrr'] = react[3]
            data["post" + str(k)]['commentaires'] = dict()
            data["post" + str(k)]['commentaires']['det'] = comment[0]
            data["post" + str(k)]['commentaires']['nbr_comm_positive'] = comment[1]
            data["post" + str(k)]['commentaires']['nbr_comm_negative'] = comment[2]
            data["post" + str(k)]['commentaires']['nbr_comm_neutre'] = comment[3]

            lp.append(data["post" + str(k)]['commentaires']['nbr_comm_positive'])
            lneg.append(data["post" + str(k)]['commentaires']['nbr_comm_negative'])
            lneu.append(data["post" + str(k)]['commentaires']['nbr_comm_neutre'])

            l_reaction.append([data["post" + str(k)]['react']['J’aime '], data["post" + str(k)]['react']['J’adore '],
                               data["post" + str(k)]['react']['Haha'], data["post" + str(k)]['react']['Grrr']])
            score_react = SentimentPost().analyse_post(l_reaction)
            score_comm = comment[4]
            overall_score = score_react + score_comm
            if overall_score > 0.5:
                conclusion = "positive"
            elif overall_score < -0.4:
                conclusion = "negative"
            else:
                conclusion = "neutre"

            data["post" + str(k)]['post_sent_overall'] = conclusion

            # insertion = Db(k, data["post" + str(k)]['titre'],data["post" + str(k)]['react']['J’aime '],data["post" + str(k)]['react']['J’adore ' ],data["post" + str(k)]['react']['Haha'], data["post" + str(k)]['react']['Grrr' ],data["post" + str(k)]['commentaires']['det'],data["post" + str(k)]['commentaires']['nbr_comm_positive'],data["post" + str(k)]['commentaires']['nbr_comm_negative'],data["post" + str(k)]['commentaires']['nbr_comm_neutre'])
            # insertion.connect()
            # insertion = Db3()
            # insertion.connect1(k,data["post" + str(k)]['titre'], data["post" + str(k)]['react']['J’aime '],data["post" + str(k)]['react']['J’adore '],data["post" + str(k)]['react']['Haha'], data["post" + str(k)]['react']['Grrr'],data["post" + str(k)]['commentaires']['nbr_comm_positive'],data["post" + str(k)]['commentaires']['nbr_comm_negative'],data["post" + str(k)]['commentaires']['nbr_comm_neutre'])

            k = k + 1

        a_sum = sum(lp)
        b_sum = sum(lneg)
        c_sum = sum(lneu)

        data["nombre de commentaire totales"] = a_sum + b_sum + c_sum

        # insertion2=DB2(data["nombre de commentaire totales" ],a_sum,b_sum,c_sum)
        # insertion2.connect2()

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=1, separators=(',', ':'))
        # df = pd.DataFrame(data).transpose()
        # df.to_csv('LBGplc.csv')
