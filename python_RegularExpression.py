# coding:utf-8

#  ------------------------
#
#   python 正则表达式
#
#  ------------------------

import re

pattern = re.compile(r'hello')  # 将正则表达式编译成Pattern对象

match = pattern.match('hello python ')    # 使用Pattern匹配文本，得到匹配结果，无结果返回None

if match:
    print match.group()  # 使用match或得分组信息

