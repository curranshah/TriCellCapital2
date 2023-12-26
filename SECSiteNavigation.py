from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup
from AdditionalFunctions import convertHedgefundName
import requests
import numpy as np
import time
import datetime
import calendar
import mysql.connector

browser = webdriver.Chrome()

def checkForPopup():
    try:
        popup = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.ID,'acsMainInvite')))
        # popup = browser.find_element_by_id('acsMainInvite')
        popup = True
        return popup
    except:
        popup = False
        return popup


def goToHedgeFundPage(hedgefundname, browser):
    # browser.get('https://www.sec.gov/cgi-bin/browse-edgar?company=ValueAct+Holdings&owner=exclude&action=getcompany')
    browser.get('https://www.sec.gov/edgar/searchedgar/companysearch.html')
    mainpage = browser.current_window_handle
    handles = browser.window_handles
    popup = checkForPopup()
    while popup == True:
        print('Popup was True')
        browser.get('https://www.sec.gov/edgar/searchedgar/companysearch.html')
        # browser.switch_to.alert()
        # browser.find_element_by_xpath('//div[@aria-label="Close Dialog"]').click()
                                      # '[@class = "acsCloseButton acsAbandonButton"]').click()
        print('Closed Popup')
        popup = checkForPopup()
        # browser.switch_to.window(browser.window_handles[0])
        # time.sleep(2)

    searchbar = browser.find_element(By.ID, "edgar-company-person")
    searchbar.clear()
    searchbar.send_keys(hedgefundname)
    # searchbar.send_keys('Lone Pine Capital LLC')
    searchbar.send_keys(Keys.ENTER)
    WebDriverWait(browser, 10).until(EC.url_contains("https://www.sec.gov/cgi-bin/browse-edgar?company="))

goToHedgeFundPage('ValueAct Holdings', browser)