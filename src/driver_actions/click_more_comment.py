from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class MoreCommentClick :
    def __init__(self , browser):
        self.browser = browser

    def show_more ( self ):
        more_comments = self.browser.find_elements_by_css_selector('._7a94._7a9d ._4sxc._42ft')
        for moreComment in more_comments:
            self.browser.implicitly_wait(5)
            action = webdriver.common.action_chains.ActionChains(self.browser)
            action.move_to_element_with_offset(moreComment, 5, 5)
            action.perform()
            moreComment.click()