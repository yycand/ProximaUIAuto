# -*-coding:utf-8-*-#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

projectlist = Element('projectlist')


class ProjectListPage(WebPage):
    """基本类"""

    def click_list(self):
        self.is_click(projectlist.get_item('项目列表'))
        sleep()


if __name__ == '__main__':
    pass
