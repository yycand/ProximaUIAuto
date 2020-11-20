#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

login = Element('login')


class LoginPage(WebPage):
    """登录类"""

    def input_username(self, username):
        self.input_text(login.get_item('用户名'), username)
        sleep()

    def input_password(self, password):
        self.input_text(login.get_item('密码'), password)
        sleep()

    def click_login(self):
        self.is_click(login.get_item('登录按钮'))
        sleep()


if __name__ == '__main__':
    pass
