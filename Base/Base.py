import os
import sys
import configparser
import time

from selenium import webdriver
import unittest
import datetime
from OrmucoTest.Utils import Utils
import logging
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

logging.basicConfig(filename=Utils.get_project_path()+'\\Result\\'+ "Result.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class BaseClass(unittest.TestCase):

    def setUp(self):
        self.driver = Utils.get_properties("browser", "name")

        if self.driver == 'chrome':
            self.driver = webdriver.Chrome(executable_path=Utils.get_project_path() + '/Drivers/chromedriver.exe')

        elif self.driver == 'ie':
            self.driver = webdriver.Chrome(executable_path=Utils.get_project_path() + '/Drivers/IEDriverServer.exe')

        elif self.driver == 'firefox':
            self.driver = webdriver.Chrome(executable_path=Utils.get_project_path() + '/Drivers/geckodriver.exe')

        else:
            self.driver = webdriver.Chrome(executable_path=Utils.get_project_path() + '/Drivers/chromedriver.exe')

        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        logger.info("Started at : " + str(datetime.datetime.now()))
        logger.info("Setting " + Utils.get_properties("browser", "name") + " browser driver")
        logger.info("*"*80)
        self.driver.get(Utils.get_properties("uat", "uat_url"))
        logger.info('********** Starting the Application **************')
        self.driver.set_page_load_timeout(Utils.PAGE_LOAD_TIMEOUT)
        time.sleep(5)


    def tearDown(self):
        if(self.driver != None):
            logger.info("*"*80)
            logger.info("Set up Destroyed")
            logger.info("Run Completed at:"+str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()







