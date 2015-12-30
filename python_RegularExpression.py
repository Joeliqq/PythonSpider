# coding:utf-8

#------------------------
#
# python 正则表达式
#
#------------------------

import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')

# 使用Pattern匹配文本，得到匹配结果，无结果返回None
match = pattern.match('hello python ')

if match:
    # 使用match或得分组信息
    print match.group()

