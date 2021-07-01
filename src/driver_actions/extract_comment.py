from src.nlp_fonctions.main_fonctions import CommentCleaning
from src.sentiment_analyszer.sentiment import SentimentAnalyzer
class CommentExtractor:
    def __init__(self, web_element):
        self.web_element = web_element

    def extract_comment(self):
        t= []
        y=[]
        p=[]
        c=[]
        commenters = self.web_element.find_elements_by_css_selector('a._6qw4')
        for commenter in commenters :
            comm = commenter.text
            t.append(comm)
        comments_text = self.web_element.find_elements_by_css_selector('span._3l3x')
        for comment_text in comments_text :
            comms = comment_text.text
            text_sample = CommentCleaning(comms)
            comment =text_sample.clean_comment()
            pos_neg = SentimentAnalyzer(comms )
            sent_com =pos_neg.analyse()
            """nbr_com = pos_neg.nbr_pos_neg_neu()
            c.append(nbr_com)
            print(c)"""
            y.append(str(comment))
            p.append(sent_com)
        u=dict()
        for x, z, m in zip(t, y,p):
            u['auteur'] = x
            u['text'] = z
            u['sent'] = m
        return u
    def extract_nbr_comment(self):
        i=0
        for web in self.web_element :

            commenters = web.find_elements_by_css_selector('a._6qw4')
            for cs in commenters :
                i=i+1
        return str(i) + "  commentaires"
