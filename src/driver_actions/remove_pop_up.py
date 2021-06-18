class BlockPopUp :
    def __init__(self , browser):
        self.browser =browser

    def remove (self):
        container = self.browser.find_element_by_class_name(u"_5hn6")
        self.browser.execute_script("arguments[0].style.display = 'none';", container)