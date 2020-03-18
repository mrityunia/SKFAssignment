# Created by ********  chomri01 at 1/23/2020

# Feature Name :: --

# To Do ::-
from selenium import webdriver
import sys
from utility.logger_report_details import *
def get_chrome_driver():
	try:
		chrome_option =  webdriver.ChromeOptions()
		chrome_option.add_argument('--disable-extensions')
		chrome_option.add_argument("--incognito-")
		driver=webdriver.Chrome(executable_path=chrome_path,chrome_options=chrome_option)
		logging.info("Chrome Driver is initiated")
		return driver
	except :
		logging.error("Some exception occurred {} ".format(str(sys.exc_info())))

def get_firefox_driver():
	try:
		firefox_option=webdriver.FirefoxOptions()
		firefox_option.add_argument("--disable-extensions")
		firefox_option.add_argument("--incognito-")
		driver=webdriver.Firefox(executable_path=firefox_path,firefox_options=firefox_option)
		logging.info("FireFox Driver is initiated ")
	except:
		logging.error("Some exception occurred {} ".format(str(sys.exc_info())))