class TextExtractor:
    def __init__(self, web_element):
        self.web_element = web_element

    def extract_text(self):
        posts = self.web_element.find_element_by_css_selector('p')
        data = posts.text
        return data






