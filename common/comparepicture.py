#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from functools import reduce

from PIL import Image
import math
import operator

from config.conf import EXCEPTPICTURE_DIR


class ComparePicture:
    @staticmethod
    def compare_picture(result_picture, except_picture):
        """
        :param except_picture:
        :param result_picture:
        :return: 返回对比的结果
        """
        result_image = Image.open(result_picture)
        except_image = Image.open(except_picture)

        result_histogram = result_image.histogram()
        except_histogram = except_image.histogram()

        differ = math.sqrt(
            reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, result_histogram, except_histogram))) / len(
                result_histogram))

        return differ


if __name__ == '__main__':
    pass
