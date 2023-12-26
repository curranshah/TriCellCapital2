from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup
from AdditionalFunctions import convertHedgefundName, checkValidClassTitle
import CIK_IDs
import pandas as pd
import requests
import numpy as np
import time
import datetime
import calendar
import mysql.connector

## This method manually enters the name of the hedgefund.  I should try and search the url by CIK ID
#
# browser = webdriver.Chrome()
# browser.get('https://www.sec.gov/edgar/searchedgar/companysearch.html')
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "edgar-company-person")))
# searchbar = browser.find_element(By.ID, "edgar-company-person")
# searchbar.clear()
# searchbar.send_keys('Lone Pine Capital LLC')
# searchbar.send_keys(Keys.ENTER)
# WebDriverWait(browser, 10).until(EC.url_contains("https://www.sec.gov/edgar/browse/"))
#
# searchtable = browser.find_element(By.ID, "search")
# searchtable.clear()
# searchtable.send_keys('13F-HR')
# searchtable.send_keys(Keys.ENTER)

## This method is to search by CIK IDs
CIK_IDs_dict = CIK_IDs.CIK_IDs_dict

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# browser = webdriver.Chrome()
# browser = webdriver.Chrome(options=chrome_options)

# ID_value = CIK_IDs_dict['ValueAct Holdings, L.P.']
# browser.get('https://www.sec.gov/edgar/browse/?CIK={ID}'.format(ID=ID_value))
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'searchbox')))
#
# searchtable = browser.find_element(By.ID, 'searchbox')
# searchtable.clear()
# searchtable.send_keys('13F-HR ')
# searchtable.send_keys(Keys.ENTER)
#
# # filingtable = browser.find_element(By.ID, 'filingsTable')
# # elements = browser.find_elements(By.CLASS_NAME, 'filing-link-all-files')
# # elements = browser.find_elements(By.PARTIAL_LINK_TEXT, 'filing')
# elements = browser.find_elements(By.PARTIAL_LINK_TEXT, 'Filing')
# # elements = browser.find_elements(By.PARTIAL_LINK_TEXT, 'Click to Open filing')
# # print(len(elements))
# links_list = []
# for elem in elements:
#     # print(elem.get_attribute("href"))
#     links_list.append(elem.get_attribute('href'))
# # print(filingtable.get_attribute('data-column')
# rows = browser.find_elements(By.XPATH, '//table[@id="filingsTable"]/tbody/tr')
# reporting_dates = []
# for row in rows:
#     reporting_date = row.text.split(' ')[-1]
#     reporting_dates.append(reporting_date)
#     # print(reporting_date)
#
# reporting_dates = list(dict.fromkeys(reporting_dates))
# link_dictionary = {}
# df2 = pd.DataFrame()
# # print(reporting_dates)
# df2['Reporting Date'] = reporting_dates
# df2['Link'] = links_list

# print(df2)
# for i in range(len(elements)):
#     print(i)
#     link_dictionary[rows[i].text.split(' ')[-1]] = elements[i].get_attribute('href')

# testlinklist1 = df2['Link'].tolist()
# browser.get(testlinklist1[0])
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'vac13f'))).click()
# testlink = 'https://www.sec.gov/Archives/edgar/data/1418814/000141881222000068/xslForm13F_X01/vac13f111422.xml.xml'
# browser.get(testlink)
# columnsC = browser.find_elements(By.CLASS_NAME, 'FormData')
# columnsR = browser.find_elements(By.CLASS_NAME, 'FormDataR')
# stocknames = []
# classtitles = []
# cusips = []
# values = []
# share_nums = []
#
# counter = 0
# for col in columnsC:
#     print(col.get_attribute('innerHTML'))
#     if counter == 0:
#         stocknames.append(col.get_attribute('innerHTML'))
#         counter += 1
#     elif counter == 1:
#         classtitles.append(col.get_attribute('innerHTML'))
#         counter += 1
#     elif counter == 2:
#         cusips.append(col.get_attribute('innerHTML'))
#         counter += 1
#     elif counter == 3:
#         counter += 1
#     elif counter == 4:
#         counter += 1
#     else:
#         counter = 0
#
# counter = 0
# for col in columnsR:
#     print(col.get_attribute('innerHTML'))
#     if counter == 0:
#         values.append(col.get_attribute('innerHTML'))
#         counter += 1
#     elif counter == 1:
#         share_nums.append(col.get_attribute('innerHTML'))
#         counter += 1
#     elif counter == 2:
#         counter += 1
#     elif counter == 3:
#         counter += 1
#     else:
#         counter = 0
#
# print(stocknames)
# print(classtitles)
# print(cusips)
# print(values)
# print(share_nums)
# data = {'Stock': stocknames, 'Class': classtitles, 'Value': values, 'Number of Shares': share_nums}
# df = pd.DataFrame(data=data)
# print()
# print(df)
#
# good_indices = checkValidClassTitle(classtitles)
# df = df.loc[df.index[good_indices]]
# df.reset_index(drop=True, inplace=True)
#
# print()
# print(df)
# pd.set_option('display.max_colwidth', None)
# print(df)

links = ['https://www.sec.gov/Archives/edgar/data/0001418814/000141881223000073/0001418812-23-000073-index.htm',
         'https://www.sec.gov/Archives/edgar/data/0001418814/000141881223000038/0001418812-23-000038-index.htm']

for i in range(len(links)):
    browser = webdriver.Chrome()
    print(i)
    browser.get(links[i])
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'vac13f'))).click()
    browser.quit()