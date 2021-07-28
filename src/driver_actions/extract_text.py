from src.nlp_fonctions.topic import Topics
class TextExtractor:
    def __init__(self, web_element):
        self.web_element = web_element

    def extract_text(self):
        try:
            posts = self.web_element.find_element_by_css_selector('p')
            data = posts.text
            post = Topics()
            topic = post.topic_model(data)
        except:
            data = "no description"
            topic = "no topic"

        return data,topic






