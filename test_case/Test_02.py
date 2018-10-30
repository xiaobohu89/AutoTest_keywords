# #!G:\python\python.exe
# # _*_coding: utf-8 _*_
# # author: huxiaobo
#
# import os
# import time
# import unittest
# from appium import webdriver
#
# class Test(unittest.TestCase):
#     def setUp(self):
#         print "initialize!"
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'
#         desired_caps['platformVersion'] = '5.1'
#         desired_caps['deviceName'] = 'LC5BTB801564'
#         desired_caps['appPackage'] = 'com.tyuan.tangy'
#         desired_caps['appActivity'] = '.ui.IndexActivity'
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#         print "open app!"
#         time.sleep(20)
#
#     def tearDown(self):
#         self.driver.quit()
#         print "close app!"
#         time.sleep(5)
#
#     def test04(self):
#         u'''设置手机铃音'''
#         self.driver.find_element_by_id("com.tyuan.tangy:id/title").click()
#         time.sleep(10)
#         self.driver.find_element_by_id("com.tyuan.tangy:id/setting").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath("// android.widget.TextView[ @ text =\"ตั้งเป็นเสียงเรียกเข้า\"]").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("com.tyuan.tangy:id/btn_sure").click()
#         time.sleep(5)
#
#     def test05(self):
#         u'''设置消息铃音'''
#         self.driver.find_element_by_id("com.tyuan.tangy:id/title").click()
#         time.sleep(10)
#         self.driver.find_element_by_id("com.tyuan.tangy:id/setting").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"ตั้งเป็นเสียงเตือน\"]").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("com.tyuan.tangy:id/btn_sure").click()
#         time.sleep(5)
#
#     def test06(self):
#         u'''设置闹钟铃音'''
#         self.driver.find_element_by_id("com.tyuan.tangy:id/title").click()
#         time.sleep(10)
#         self.driver.find_element_by_id("com.tyuan.tangy:id/setting").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"ตั้งเป็นเสียงนาฬิกาปลุก\"]").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("com.tyuan.tangy:id/btn_sure").click()
#         time.sleep(5)
#
# if __name__ == '__main__':
#     unittest.main()
