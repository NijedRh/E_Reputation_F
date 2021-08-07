import time
#import schedule
from src.driver_actions.extract_page import PageExtractor

def main_process():
    page = PageExtractor("https://www.facebook.com/LBGplc")
    page.scrap_fb()
#schedule.every().monday.at('08:00').do(main_process)
if __name__ == '__main__':
     main_process()
"""while True :

        schedule.run_pending()
        time.sleep(1)"""

