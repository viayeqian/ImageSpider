from util.util import Util
from engine.engine import Engine
import time


class Bing(Engine):
    def __init__(self, web_driver, start_url, storing_folder):
        Engine.__init__(self, web_driver)
        self.start_url = start_url
        self.storing_folder = storing_folder

    def retrieve_image(self):
        Engine.retrieve_image(self)
        self.web_driver.get(self.start_url)

        url = self.web_driver.find_element_by_class_name("mainImage accessible nofocus")
        current_index = 0
        while url is not None:
            url = url.get_attribute('src')
            image_format = url.split('.')[-1]
            print('IMAGE URL: ', url)
            image_name = str(current_index) + '.' + image_format
            if Util.download_image(url, self.storing_folder, image_name):
                current_index += 1
            self.web_driver.find_elements_by_class_name("iv_button")[1].click()
            time.sleep(3)
            url = self.web_driver.find_element_by_class_name("mainImage accessible nofocus")
