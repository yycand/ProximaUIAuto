#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from config.conf import RESULTSCREENSHOT_DIR
from tools.times import datetime_strftime


class Screen:

    @staticmethod
    def set_result_picture_path(test_case_name):
        picture_time = datetime_strftime("%Y-%m-%d-%H_%M_%S")
        directory_time = datetime_strftime("%Y-%m-%d")
        file_path = os.path.join(RESULTSCREENSHOT_DIR, directory_time)
        try:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
        except BaseException as msg:
            print(msg)

        result_picture_path = file_path+"\\" + test_case_name + picture_time + ".png"
        return result_picture_path


if __name__ == '__main__':
    pass
