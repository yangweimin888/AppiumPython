# -*- coding:utf-8 -*-
# @Time   : 2018-11-01 19:24
# @Author : YangWeiMin

from Page.BasePage import Action

class Logout(Action):
    '''退出页面'''
    # 用户中心
    user_loc = ('id', 'com.koubei.mobile.o2o.personal:id/tab_flag')
    # 设置中心
    setting_loc = ('id', 'com.koubei.mobile.o2o.personal:id/settingContent')
    # 退出
    logout_loc = ('id', 'com.koubei.mobile.o2o.personal:id/logout')
    # 确认退出
    confirm_loc = ('id', 'android:id/button1')

    def click_user(self):
        '''进入个人中心'''
        self.click_button(self.user_loc)

    def click_setting(self):
        '''进入设置页面'''
        self.click_button(self.setting_loc)

    def click_logout(self):
        '''点击退出登录按钮'''
        self.click_button(self.logout_loc)

    def click_confirm_logout(self):
        self.click_button(self.confirm_loc)
