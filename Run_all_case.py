#!G:\python\python.exe
# _*_coding: utf-8 _*_
# author: huxiaobo

import os
import time
import unittest
import HTMLTestRunner
from Auto_gajj.config import globalparameter as gl
from Auto_gajj.src.commom import send_mail
from appium import webdriver

discover = unittest.defaultTestLoader.discover(gl.test_case_path,pattern='test_*.py',top_level_dir=None)
# print discover

if __name__=='__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # report_path = 'E:\\Work\\Workspace-python\\Test_guanaijiajia\\report\\'
    filename = gl.report_path + now + '_Report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'关爱加加功能自动化测试执行结果:')
    runner.run(discover)
    fp.close()
    # 发送邮件
    time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕（这里被坑了＝＝）
    email = send_mail.send_email()
    email.sendReport()
