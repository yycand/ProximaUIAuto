#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
from selenium.webdriver.support.ui import Select

base = Element('systembase')


class SystemBasePage(WebPage):
    # 切换frame
    def switch_to_frame(self):
        self.driver.switch_to.frame(self.find_element(base.get_item('切换frame')))
        sleep()

    # 切换到默认页
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    # 系统标签
    def click_elements(self, key, index):
        self.find_elements(base.get_item(key))[index].click()
        sleep()

    # 基本标签
    def click_base(self, key):
        self.is_click(base.get_item(key))
        sleep()

    # 下拉框选择
    def select_option(self, select_key, value_key):
        Select(self.find_element(base.get_item(select_key))).select_by_value(value_key)
        sleep()

    # 下拉框获取值
    def get_option(self, select_key):
        return Select(self.find_element(base.get_item(select_key))).first_selected_option.text

    # 输入值
    def input_loadingvideourl(self, input_loadingvideourl):
        self.input_text(base.get_item('动画加载路径'), input_loadingvideourl)
        sleep()

    # 保存
    def click_save(self):
        self.is_click(base.get_item('保存'))
        sleep()

    # 获取checkbox值
    def find_checkbox_value(self, key):
        return self.find_element(base.get_item(key)).get_attribute('value')

    # 截图
    def save_picture(self, picture_path):
        self.driver.save_screenshot(picture_path)


if __name__ == '__main__':
    pass
