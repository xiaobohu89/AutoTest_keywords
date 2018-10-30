#!/user/bin/python
# -*- coding: UTF-8 -*-
# author: huxiaobo
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
#连接设备
device = MonkeyRunner.waitForConnection(3,"b2b4487b")
#启动app
device.startActivity("com.example.aerospace/com.example.aerospace.ui.ActivityIndex")
MonkeyRunner.sleep(3)
#点击登录按钮
device.touch(500,1000,"Down_AND_UP")
MonkeyRunner.sleep(2)
#点击密码输入框
device.touch(500,700,"Down_AND_UP")
MonkeyRunner.sleep(2)
#输入登录密码
device.type("888888")
MonkeyRunner.sleep(2)
#点击键盘完成按钮收起键盘
device.touch(940,1110,"Down_AND_UP")
MonkeyRunner.sleep(2)
#点击登录按钮
device.touch(500,1150,"Down_AND_UP")
MonkeyRunner.sleep(5)
#截图
image = device.takeSnapshot()
image.writeToFile('E:\Work\Workspace-python\AutoTest\image\\test_web.png',"png")





