"""
this program split urls to each specific football club/league/country.
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import requests
from selenium.webdriver.chrome.options import Options

import configWS

class GetLeagueUrls:
    def __init__(self, url):
        self.selenium_driver = get_data_from_url(url)

    def get_country_name(self):
        """
        return: the name of country.
        """
        # c_idx = COUNTRY_IDX
        c_idx = 1
        country_name = self.selenium_driver.find_element_by_class_name("tournament").find_elements(By.TAG_NAME, "a")[
            c_idx].text.title()
        return country_name

    def get_league_name(self):
        """ return the name of league. """
        # l_idx = LEAGUE_IDX
        l_idx = 2
        league_name = self.selenium_driver.find_element_by_class_name("tournament").find_elements(By.TAG_NAME, "a")[
            l_idx].text.title()
        return league_name

    def get_club_urls_list(self):
        """
        :param:url_of_club get selenium driver of league page.
        :returns club urls list and league name.
        """
        club_urls_list = []

        club_element_list = self.selenium_driver.find_elements_by_xpath("//table[@id='table-type-1']/tbody/tr")
        for club_elm in club_element_list:
            onclick_atr = club_elm.find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "a").get_attribute(
                "onclick")
            url_of_club = onclick_atr.split("'/")[1].split(r"\'")[0][:-3]
            full_url_of_club = "https://www.scoreboard.com/" + url_of_club + "squad"
            club_urls_list.append(full_url_of_club)
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
    :param:selenium_driver function loads url
    :return object that contain all html data.
    """

    options = Options()
    options.headless = True  # disable open website.
    selenium_driver = webdriver.Chrome(chrome_options=options)
    selenium_driver.get(url)

    return selenium_driver


def check_have_squad(url):
    """ checks if the club contains data about the players """
    checked_url = requests.get(url)
    if checked_url.status_code == 200:
        return True
    else:
        return False
