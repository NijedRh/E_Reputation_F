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
                t['J’aime '] =  reaction
            elif "J’adore" in reaction :
                t['J’adore ' ]= reaction
            elif "Haha" in reaction :
                t['Haha'] = reaction
            elif "Grrr" in reaction :
                t['Grrr' ]= reaction
        return t
