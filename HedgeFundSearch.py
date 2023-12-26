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
import CIK_IDs
import pandas as pd
import requests
import numpy as np
import time
import datetime
import calendar
import mysql.connector

## Defining functions related to using CIK IDs to get tables
hedgefundname = 'ValueAct Holdings, L.P.'
CIK_IDs_dict = CIK_IDs.CIK_IDs_dict
def get13FLinks(hedgefundname, id_dictionary):
    links_list = []
    reporting_dates = []
    link_dictionary = {}
    df1 = pd.DataFrame()

    ID_value = id_dictionary[hedgefundname]
    browser = webdriver.Chrome()
    browser.get('https://www.sec.gov/edgar/browse/?CIK={ID}'.format(ID=ID_value))
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'searchbox')))

    searchtable = browser.find_element(By.ID, 'searchbox')
    searchtable.clear()
    searchtable.send_keys('13F-HR ')
    searchtable.send_keys(Keys.ENTER)

    links = browser.find_elements(By.PARTIAL_LINK_TEXT, 'Filing')
    for elem in links:
        links_list.append(elem.get_attribute('href'))
    rows = browser.find_elements(By.XPATH, '//table[@id="filingsTable"]/tbody/tr')
    for row in rows:
        reporting_date = row.text.split(' ')[-1]
        reporting_dates.append(reporting_date)


    reporting_dates = list(dict.fromkeys(reporting_dates))
    df1['Reporting Date'] = reporting_dates
    df1['Link'] = links_list
    browser.quit()
    return df1

def get13FTableInformation(dataframe):
    links = dataframe['Link'].tolist()
    return_dict = {}
    for i in range(len(links)):
        data = {}
        print(i)
        print(links[i])
        browser = webdriver.Chrome()
        browser.get(links[i])
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'vac13f'))).click()
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'FormData')))
        columnsC = browser.find_elements(By.CLASS_NAME, 'FormData')
        columnsR = browser.find_elements(By.CLASS_NAME, 'FormDataR')
        stocknames = []
        classtitles = []
        cusips = []
        values = []
        share_nums = []

        counter = 0
        for col in columnsC:
            print(counter)
            if counter == 0:
                stocknames.append(col.get_attribute('innerHTML'))
                counter += 1
            elif counter == 1:
                classtitles.append(col.get_attribute('innerHTML'))
                counter += 1
            elif counter == 2:
                cusips.append(col.get_attribute('innerHTML'))
                counter += 1
            elif counter == 3:
                counter += 1
            elif counter == 4:
                counter += 1
            else:
                counter = 0

        counter = 0
        for col in columnsR:
            if counter == 0:
                values.append(col.get_attribute('innerHTML'))
                counter += 1
            elif counter == 1:
                share_nums.append(col.get_attribute('innerHTML'))
                counter += 1
            elif counter == 2:
                counter += 1
            elif counter == 3:
                counter += 1
            else:
                counter = 0

        data = {'Stock': stocknames, 'Class': classtitles, 'Value': values, 'Number of Shares': share_nums}
        df = pd.DataFrame(data=data)
        print(df)
        return_dict[dataframe['Reporting Date'].tolist()[i]] = df
        browser.quit()
    return return_dict


df1 = get13FLinks(hedgefundname, CIK_IDs_dict)
pd.set_option('display.max_colwidth', None)
# print(df1)

test_dict = get13FTableInformation(df1)
print(test_dict)

