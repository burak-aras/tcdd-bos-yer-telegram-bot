from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class driver():

    def __init__(self, path, nereden, nereye, zaman):
        self.path = path
        self.nereden = nereden
        self.nereye = nereye
        self.zaman = zaman

    def sourceCode(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(self.path, options=options)
        driver.get(
            "https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")
        nereden = driver.find_element("id", "nereden")
        nereden.send_keys(self.nereden)
        nereye = driver.find_element("id", "nereye")
        nereye.send_keys(self.nereye)
        zaman = driver.find_element("id", "trCalGid_input")
        zaman.send_keys(Keys.CONTROL + "a")
        zaman.send_keys(Keys.DELETE)
        zaman.send_keys(self.zaman)
        driver.find_element(
            "xpath", "/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div/form/div[3]/p[3]/button/span").click()
        time.sleep(9)
        return driver.page_source
