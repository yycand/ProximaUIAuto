#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import os

import allure
import pytest

from common.comparepicture import ComparePicture
from common.reades import es
from config.conf import EXCEPTPICTURE_DIR
from tools.times import sleep
from common.readexcel import ParseExcel
from common.screen import Screen
from page_object.systembasepage import SystemBasePage

bd = ParseExcel('base')


@allure.feature("测试系统基本模块")
class TestSystemBase:

    # @pytest.mark.parametrize("test_input", ParseExcel.get_excel_data(bd, 'base'))
    # @allure.story("前台调试")
    # def test_debug_js(self, drivers, test_input):
    #     """前台调试"""
    #     base = SystemBasePage(drivers)
    #     base.switch_to_frame()
    #     base.click_elements('系统', 0)
    #     base.click_base('基本')
    #     resall = es.get('uino_proxima_sys_configure', 5200557462705519, 'uino_proxima_sys_configure')
    #     res = json.loads(resall['_source']['value'])
    #     if res['debugJs']:
    #         base.click_base('前台调试')
    #         base.click_save()
    #         base.refresh()
    #         base.switch_to_frame()
    #         base.click_elements('系统', 0)
    #         base.click_base('基本')
    #         resallt = es.get('uino_proxima_sys_configure', 5200557462705519, 'uino_proxima_sys_configure')
    #         rest = json.loads(resallt['_source']['value'])
    #         assert not rest['debugJs']
    #     else:
    #         base.click_base('前台调试')
    #         base.click_save()
    #         base.refresh()
    #         base.switch_to_frame()
    #         base.click_elements('系统', 0)
    #         base.click_base('基本')
    #         resallf = es.get('uino_proxima_sys_configure', 5200557462705519, 'uino_proxima_sys_configure')
    #         resf = json.loads(resallf['_source']['value'])
    #         assert resf['debugJs']
    #     # base.click_elements('拾取控制和加载配置', 0)
    #     # base.click_base('拾取控制取消')
    #     # base.click_elements('拾取控制和加载配置', 1)
    #     # base.click_base('加载配置取消')
    #     # base.select_option('过场动画', test_input["valueKey"])
    #     # base.input_loadingvideourl(test_input["loadingvideourl"])
    #     # base.click_base('模型贴图')
    #     # base.click_base('静态模型')
    #     # base.click_base('顶层设备')
    #     # base.click_base('自定义布局')
    #     # base.click_base('隐藏地图')
    #     # base.click_base('批量渲染')
    #
    # @pytest.mark.parametrize("test_input", ParseExcel.get_excel_data(bd, 'base'))
    # @allure.story("提示框")
    # def test_is_show_alert(self, drivers, test_input):
    #     """提示框"""
    #     base = SystemBasePage(drivers)
    #     base.click_elements('系统', 0)
    #     base.click_base('基本')
    #     resall = es.get('uino_proxima_sys_configure', 5200557462705519, 'uino_proxima_sys_configure')
    #     res = json.loads(resall['_source']['value'])
    #     if res['isShowAlert']:
    #         base.click_base('提示框')
    #         base.click_save()
    #         base.refresh()
    #         base.switch_to_frame()
    #         base.click_elements('系统', 0)
    #         base.click_base('基本')
    #         resallt = es.get('uino_proxima_sys_configure', 5200557462705519, 'uino_proxima_sys_configure')
    #         rest = json.loads(resallt['_source']['value'])
    #         assert not rest['isShowAlert']
    #     else:
    #         base.click_base('提示框')
    #         base.click_save()
    #         base.refresh()
    #         base.switch_to_frame()
    #         base.click_elements('系统', 0)
    #         base.click_base('基本')
    #         resallf = es.get('uino_proxima_sys_configure', 5200557462705519, 'uino_proxima_sys_configure')
    #         resf = json.loads(resallf['_source']['value'])
    #         assert resf['isShowAlert']

    @pytest.mark.parametrize("test_input", ParseExcel.get_excel_data(bd, 'base'))
    @allure.story("主题样式")
    def test_theme(self, drivers, test_input):
        """主题样式"""
        base = SystemBasePage(drivers)
        base.switch_to_frame()
        base.click_elements('系统', 0)
        base.click_base('基本')
        base.select_option('主题样式', '大表姐')
        base.click_save()
        base.refresh()
        base.switch_to_frame()
        base.click_elements('系统', 0)
        base.click_base('基本')
        assert '大表姐' == base.get_option('主题样式')
        base.switch_to_default_content()
        base.click_base('项目列表')
        base.click_base('优锘产业园')
        sleep(40)
        result_picture_path = Screen.set_result_picture_path('主题样式')
        base.save_picture(result_picture_path)
        except_picture_path = EXCEPTPICTURE_DIR + "\\" + "主题样式" + "\\" + "主题样式.png"
        differ = ComparePicture.compare_picture(result_picture_path, except_picture_path)
        assert differ < 300


if __name__ == '__main__':
    pytest.main(['TestCase/test_systembase.py', '--alluredir', './allure_report/allure'])
    os.system('allure serve allure_report/allure')
