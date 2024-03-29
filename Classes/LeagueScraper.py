"""
this program split urls to each specific football club/league/country.
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import requests
from Constants import *


class LeagueScraper:
    def __init__(self, url):
        self.selenium_driver = get_data_from_url(url)

    def get_country_name(self):
        """ return: the name of country. """

        country_name = self.selenium_driver.find_element_by_class_name("tournament").find_elements(By.TAG_NAME, "a")[
            COUNTRY_IDX].text.title()
        return country_name

    def get_league_name(self):
        """ return: the name of league. """

        league_name = self.selenium_driver.find_element_by_class_name("tournament").find_elements(By.TAG_NAME, "a")[
            LEAGUE_IDX].text.title()
        return league_name

    def get_club_urls_list(self):
        """
            Params: url_of_club get selenium driver of league page.
            Returns: club urls list and league name.
        """
        club_urls_list = []

        club_element_list = self.selenium_driver.find_elements_by_xpath("//table[@id='table-type-1']/tbody/tr")
        for club_elm in club_element_list:
            onclick_atr = club_elm.find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "a").get_attribute(
                "onclick")
            url_of_club = onclick_atr.split("'/")[1].split(r"\'")[0][:-3]
            full_url_of_club = "https://www.scoreboard.com/" + url_of_club + "squad"
            if check_have_squad(full_url_of_club):
                club_urls_list.append(full_url_of_club)

        return club_urls_list

    def close_get_data(self):
        """
            close the connect to url
        """
        self.selenium_driver.close()


def get_data_from_url(url):
    """
        Param: selenium_driver function loads url
        Return: object that contain all html data.
    """

    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    selenium_driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROME_DRIVER_PATH)
    selenium_driver.get(url)

    return selenium_driver


def check_have_squad(url):
    """ checks if the club contains data about the players.
            Params: url of club
            Return: True if the club have squad. """
    checked_url = requests.get(url)
    if checked_url.status_code == 200:
        return True
    else:
        return False
