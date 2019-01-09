# -*- coding:utf-8 -*-
# @Time   : 2018-11-13 14:19
# @Author : YangWeiMin

import unittest
from Page.LogoutPage import Logout
import time
from common.logger import Log

class CaseLogout(Logout,unittest.TestCase):
    log = Log()
    def test_logout_success(self):
        '''正常退出'''
        try:
            self.click_user()
            time.sleep(2)
            self.click_setting()
            self.click_logout()
            time.sleep(2)
            self.click_confirm_logout()
            self.log.info('退出成功')
        except Exception as e:
            self.getScreenShot()
            self.log.error(e)

if __name__ == '__main__':
    unittest.main()