from src.sentiment_analyszer.sentiment_post import SentimentPost
class ReactExtractor :
    def __init__(self , web_element):
        self.web_element = web_element
    @property
    def extract_react (self):
        t=dict()
        reaction_div = self.web_element.find_elements_by_css_selector('span._1n9k')
        for reactions in reaction_div :
            reaction = reactions.find_element_by_css_selector('a').get_attribute("aria-label")
            if "J’aime" in reaction :
                t['J’aime '] = int(str( reaction.strip("J’aime").replace(" K", "000").replace(",","")))
            elif "J’adore" in reaction :
                t['J’adore ' ]= int(str(reaction.strip("J’adore")))
            elif "Haha" in reaction :
                t['Haha'] = int(str(reaction.strip("Haha")))
            elif "Grrr" in reaction :
                t['Grrr' ]= int(str(reaction.strip("Grrr")))
        post_sent=SentimentPost(t)
        sent_post = post_sent.analyse_post()
        print(sent_post)


        return t

