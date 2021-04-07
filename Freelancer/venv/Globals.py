from selenium import webdriver
import random
import time
import allure
import pytest
import selenium
from allure_commons.types import AttachmentType
from faker import Faker
import urllib

# Chrome drivers  -------------------------------------------------------------------------------------
from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True
# driver = webdriver.Chrome(options=chrome_options, executable_path="C:/webdrivers/chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:/webdrivers/chromedriver.exe")

# Firefox drivers -------------------------------------------------------------------------------------
# from selenium.webdriver.firefox.options import Options
# chrome_options = Options()
# chrome_options.headless = False
# driver = webdriver.Firefox(options=chrome_options, executable_path="C:/webdrivers/geckodriver.exe")
# driver = webdriver.Firefox(executable_path="C:/webdrivers/geckodriver.exe")


#Run tests
#pytest --alluredir=/tmp/my_allure_results TestCases.py
#Allure Serve
#allure serve /tmp/my_allure_results