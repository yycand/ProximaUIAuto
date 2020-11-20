#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from selenium.webdriver.common.by import By

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 配置文件
INI_PATH = os.path.join(BASE_DIR, 'config', 'config.ini')

# 页面元素目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# 报告目录
REPORT_PATH = os.path.join(BASE_DIR, 'allure_report', 'allure_report.html')

# 错误截图目录
SCREENSHOT_DIR = os.path.join(BASE_DIR, 'screen_capture')

# 用例数据目录
EXCEL_PATH = os.path.join(BASE_DIR, 'data')

# 操作结果截图目录
RESULTSCREENSHOT_DIR = os.path.join(BASE_DIR, 'picture')

# 期望图片
EXCEPTPICTURE_DIR = os.path.join(BASE_DIR, 'except_picture')

# 元素定位的类型
LOCATE_MODE = {
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'class': By.CLASS_NAME
}

if __name__ == '__main__':
    pass
