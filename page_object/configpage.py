#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

config = Element('config')


class ConfigPage(WebPage):
    """基本类"""
    def click_config(self):
        self.is_click(config.get_item('配置管理'))
        sleep()


if __name__ == '__main__':
    pass
