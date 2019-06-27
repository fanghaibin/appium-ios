import time
from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger


class ALLMyGroup(BasePage):
    """我的所有群聊"""
    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.GroupChatSearchActivity'

    __locators = {
        '返回': (MobileBy.ACCESSIBILITY_ID, 'back'),
        '搜索群组': (MobileBy.ACCESSIBILITY_ID, '搜索群组'),
        '创建群聊': (MobileBy.ACCESSIBILITY_ID, 'cc chat create group'),
        '群聊列表1': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]'),
        # '列表项': (MobileBy.XPATH, '//*[@resource-id="com.chinasofti.rcs:id/recyclerView"]/*'),
        # '群名': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_name'),

        #搜索群组页面
        '搜索群组1': (MobileBy.XPATH, '(//XCUIElementTypeSearchField[@name="搜索群组"])[1]'),
        '清除搜索内容': (MobileBy.ACCESSIBILITY_ID, '	cc contacts delete pressed'),
        '搜索结果': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell'),
        #创建群聊
        '清除文本': (MobileBy.ACCESSIBILITY_ID, '清除文本'),
        '请输入群聊名称': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField/XCUIElementTypeTextField'),
        '创建': (MobileBy.ACCESSIBILITY_ID, '创建'),

    }

    @TestLogger.log('点击返回')
    def click_back(self):
        self.click_element(self.__locators['返回'])

    @TestLogger.log('输入搜索关键字')
    def input_search_keyword(self, keyword):
        self.input_text(self.__locators['搜索群组'], keyword)

    @TestLogger.log('点击创建群组')
    def click_creat_group(self):
        self.click_element(self.__locators['创建群聊'])

    @TestLogger.log('通过名字选择群聊')
    def select_group_by_name(self,name):
        locator=(MobileBy.ACCESSIBILITY_ID,"'%s'" % name)
        self.click_element(locator)





#创建群组
    @TestLogger.log('点击清除群组名称')
    def click_clear_group_name(self):
        self.click_element(self.__locators['清除文本'])

    @TestLogger.log('输入搜索关键字')
    def input_group_name(self, keyword):
        self.input_text(self.__locators['请输入群聊名称'], keyword)


    @TestLogger.log('点击创建')
    def click_sure_creat(self):
        self.click_element(self.__locators['创建'])
