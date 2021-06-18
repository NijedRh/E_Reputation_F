from src.driver_actions.extract_page import PageExtractor


def main_process():
    page = PageExtractor("https://www.facebook.com/societegenerale")
    page.scrap_fb()


if __name__ == '__main__':
    main_process()
