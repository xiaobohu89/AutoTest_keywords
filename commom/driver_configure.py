#!G:\python\python.exe
# _*_coding: utf-8 _*_
# author: huxiaobo
'''
description:driver配置
'''
from appium import webdriver

class driver_configure():
    def get_driver(self):
        '''获取driver'''
        try:
            self.desired_caps = {}
            self.desired_caps['platformName'] = 'Android'  # 平台
            self.desired_caps['platformVersion'] = '4.4'  # 系统版本
            # self.desired_caps['app'] = 'E:/autotestingPro/app/UCliulanqi_701.apk'   # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
            self.desired_caps['appPackage'] = 'com.ithooks.android.ccbxreap'     # APK包名
            self.desired_caps['appActivity'] = 'com.ithooks.android.ccbxreap.ui.index.ActivityIndex'     # 被测程序启动时的Activity
            self.desired_caps['unicodeKeyboard'] = 'true'   # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
            self.desired_caps['resetKeyboard'] = 'true' # 是否在测试结束后将键盘重轩为系统默认的输入法。
            self.desired_caps['newCommandTimeout'] = '180' # Appium服务器待appium客户端发送新消息的时间。默认为60秒
            # self.desired_caps['deviceName'] = 'b2b4487b'     # vivo手机ID
            self.desired_caps['deviceName'] = 'HC44XWM03033'# htc手机ID
            self.desired_caps['noReset'] = True # true:不重新安装APP，false:重新安装app
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desired_caps)
            return self.driver
        except Exception as e:
            raise e