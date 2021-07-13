from src.nlp_fonctions.main_fonctions import CommentCleaning
from src.sentiment_analyszer.sentiment_comment import SentimentAnalyzer
class CommentExtractor:

    def __init__(self, web_element):
        self.web_element = web_element

    def extract_comment(self):
        t=[]
        y=[]
        p=[]
        lis = []
        li_comm=[]
        i=j=k=0
        commenters = self.web_element.find_elements_by_css_selector('a._6qw4')
        for commenter in commenters :
            comm = commenter.text
            t.append({"auteur " : comm})
        comments_text = self.web_element.find_elements_by_css_selector('span._3l3x')
        for comment_text in comments_text :
            comms = comment_text.text
            text_sample = CommentCleaning(comms)
            comment =text_sample.clean_comment()
            pos_neg = SentimentAnalyzer(comms)
            sent_com =pos_neg.analyse()[0]
            sent_sum =pos_neg.analyse()[1]

            sent_compound=pos_neg.analyse()[2]
            li_comm.append(float(sent_compound))


            if sent_sum =="po": i+=1
            elif sent_sum=="neg": j+=1
            else :  k+=1
            y.append({"comm " : str(comment)})
            p.append({"sent : " : sent_com})
        somme = sum(li_comm)*0.7
        for x, z, m in zip(t, y,p):
           lis.append([x,z,m])
        return lis ,i,j,k ,somme
    def extract_nbr_comment(self):
        i=0
        for web in self.web_element :
            commenters = web.find_elements_by_css_selector('a._6qw4')
            for cs in commenters :
                i=i+1
        return i
