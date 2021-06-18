from src.nlt_fonctions.main_fonctions import CommentCleaning
class CommentExtractor:
    def __init__(self, web_element):
        self.web_element = web_element

    def extract_comment(self):
        t= []
        y=[]
        commenters = self.web_element.find_elements_by_css_selector('a._6qw4')
        for commenter in commenters :
            comm = commenter.text
            t.append('auteur : ' +comm)
        comments_text = self.web_element.find_elements_by_css_selector('span._3l3x')
        for comment_text in comments_text :

            comms = comment_text.text
            text_sample = CommentCleaning(comms)
            comment =text_sample.clean_comment()
            y.append('text : ' + str(comment))
        u=[]
        for x, z in zip(t, y):
            u.append([ x,z])
        return u