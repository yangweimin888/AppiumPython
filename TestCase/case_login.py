# -*- coding:utf-8 -*-
# @Time   : 2018-11-05 19:48
# @Author : YangWeiMin

import unittest
from Page.LoginPage import Login
import time
from common.logger import Log

class CaseLogin(Login,unittest.TestCase):

    log = Log()

    def test_login_success(self):
        '''正常登录'''
        try:
            self.input_username()
            self.input_pwd()
            self.click_login()
            time.sleep(5)
            self.assertEqual(self.login_success(),'首页')
            self.log.info('登录成功')
        except Exception as e:
            self.getScreenShot()
            self.log.error(e)


if __name__ == '__main__':
    unittest.main()