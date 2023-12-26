from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import os.path
import seaborn as sns
import datetime
import calendar
import mysql.connector
from scipy.signal import argrelextrema
from operator import itemgetter
sns.set(font_scale=1.2)

def scrollToBottom(scrollpausetime):
    scrollpausetime = scrollpausetime
    browser = webdriver.Chrome()
    # Get scroll height
    lastheight = browser.execute_script("return document.documentElement.scrollHeight")
    breaker = 0

    while breaker == 0:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        # Wait to load page
        time.sleep(scrollpausetime)

        # Calculate new scroll height and compare with last scroll height
        newheight = browser.execute_script("return document.documentElement.scrollHeight")
        # print('The last height was: ' + str(lastheight))
        # print('The new height is: ' + str(newheight))
        if newheight == lastheight:
            breaker = 1
        lastheight = newheight

def convertHedgefundName(hedgefundname):
    name = hedgefundname.replace(' ','')
    name = name.replace('/','')
    name = name.replace(r'"\"', '')
    name = name.replace('.','')
    name = name.replace(',','')
    databasename = name.lower()
    return name, databasename

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))

def checkValidClassTitle(listofsecurityclass):
    accepted_classes = ['COM CL A', 'CL A', 'COM NEW', 'COM', 'COM', 'ORD SHS', 'COM', 'CL B', 'COM CL B']
    bad_indices = []
    good_indices = []
    index = 0
    for elem in listofsecurityclass:
        if elem in accepted_classes:
            good_indices.append(index)
        index += 1
    return good_indices