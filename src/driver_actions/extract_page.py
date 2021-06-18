from src.driver_actions.save_data import SavingData
from src.driver_actions.click_more_comment import MoreCommentClick
from src.driver_actions.remove_pop_up import BlockPopUp
from src.driver_actions.webdriver import WebDriver

class PageExtractor:
    def __init__(self, page_url ):
        self.page_url = page_url

    def scrap_fb(self):
        web_url = WebDriver(self.page_url)
        web_driver = web_url.driver()
        #disable pop-up
        remove_pop_up = BlockPopUp(web_driver)
        remove_pop_up.remove()
        #clicker le champ de publication
        web_driver.find_element_by_class_name('_4b4x').click()
        #disable pop-up encore une fois
        remove_pop_up.remove()
        #clicker sur tous "afficher autres commentaires"
        show_more_comment = MoreCommentClick(web_driver)
        show_more_comment.show_more()
        list_web_element= web_driver.find_elements_by_xpath('//div[@class="_4-u2 _4-u8"]')
        save = SavingData(list_web_element)
        save.save_data()