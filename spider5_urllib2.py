__author__ = 'L'
# -*- coding: utf-8 -*-

import urllib2

# 创建一个密码管理者
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
# 添加用户名和密码
top_level_url = "http://example.com/foo/"
# 如果知道 realm, 我们可以使用他代替 ``None``.
password_mgr.add_password(None, top_level_url, 'xxx', '123')

# 创建一个新的hadndler
handler = urllib2.buid