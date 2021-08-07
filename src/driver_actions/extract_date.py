class DateExtractor :
    def __init__(self, web_element) :
        self.web_element = web_element

    def extract_date(self):
        datee = self.web_element.find_element_by_class_name('_5ptz').get_attribute("title")

        return datee