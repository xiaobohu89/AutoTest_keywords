# author: huxiaobo 
# _*_coding: utf-8 _*_

from datetime import date,datetime
import os
import logging
import xlrd,xlwt
import AutoTest_keywords.config.globalparameter
import AutoTest_keywords.src
from appium import webdriver

def read_excel():
    #文件位置
    ExcelFile = xlrd.open_workbook(r'E:\\Work\\Workspace-python\\\AutoTest_keywords\\src\\TestCase.xlsx')
    #获取目标EXCEL文件sheet名
    # print (ExcelFile.sheet_names())
#------------------------------------
#若有多个sheet，则需要指定读取目标sheet例如读取sheet2
#sheet2_name=ExcelFile.sheet_names()[1]
#------------------------------------
#获取sheet内容【1.根据sheet索引2.根据sheet名称】
#sheet=ExcelFile.sheet_by_index(1)
    sheet = ExcelFile.sheet_by_name('Sheet1')

#打印sheet的名称，行数，列数
    # print (sheet.name,sheet.nrows,sheet.ncols)

#获取整行或者整列的值
    rows = sheet.row_values(0)#第一行内容
    cols = sheet.col_values(0)#第二列内容
    # print (cols,rows)

#获取单元格内容
    for x in range(sheet.nrows):
        for y in range(sheet.ncols):
            print (sheet.cell(x,y).value.encode('utf-8'))
            # print sheet.cell_value(x,y).encode('utf-8')
            # print sheet.row(0)[1].value.encode('utf-8')

#打印单元格内容格式
        # print sheet.cell(0,0).ctype
        Case_ID = sheet.cell(x,0).value.encode('utf-8')
        method  = sheet.cell(x,1).value.encode('utf-8')
        element = sheet.cell(x,2).value.encode('utf-8')
        element_path = sheet.cell(x,3).value.encode('utf-8')
        keywords_option = sheet.cell(x,4).value.encode('utf-8')
        keywords_value = sheet.cell(x,5).value.encode('utf-8')
        result = sheet.cell(x,6).value.encode('utf-8')
        print(Case_ID,method,element,element_path,keywords_option,keywords_value,result)

if __name__ =='__main__':
    read_excel()
