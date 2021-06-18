class ReactExtractor :
    def __init__(self , web_element):
        self.web_element = web_element
    @property
    def extract_react (self):
        t=[]
        reaction_div = self.web_element.find_elements_by_css_selector('span._1n9k')
        for reactions in reaction_div :
            reaction = reactions.find_element_by_css_selector('a').get_attribute("aria-label")
            t.append( reaction)
        return t