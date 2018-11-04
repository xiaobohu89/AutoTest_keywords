#!G:\python\python.exe
# _*_coding: utf-8 _*_
# author: huxiaobo

import os
import time
import logging
import unittest
from appium import webdriver
from AutoTest_keywords.commom import driver_configure
from AutoTest_keywords.commom import runlog
from AutoTest_keywords.commom import ReadExcel

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dconfigur = driver_configure.driver_configure()
        cls.driver = dconfigur.get_driver()

    def getExcel(self):
        self.driver.find_element()


    def tearDown(self):
        if self.driver != '':
            self.driver.quit()
            print('The app is closed successfully, good job man!!!"')
        else:
            print('No app is running, fail to close app... ')
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
