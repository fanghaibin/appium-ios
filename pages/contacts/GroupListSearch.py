import time
from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger


class GroupListSearchPage(BasePage):
    """搜索群组"""
    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.GroupChatSearchActivity'

    __locators = {
        '返回': (MobileBy.IOS_PREDICATE, 'name=="back"'),
        '输入关键字搜索': (MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeSearchField"'),
        '删除关键字': (MobileBy.ID, 'com.chinasofti.rcs:id/iv_clear'),
        '搜索结果列表': (MobileBy.ID, 'com.chinasofti.rcs:id/recyclerView'),
        '列表项': (MobileBy.XPATH, '//*[@resource-id="com.chinasofti.rcs:id/recyclerView"]/*'),
        '群名': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_name'),
    }

    @TestLogger.log('点击返回')
    def click_back(self):
        self.click_element(self.__locators['返回'])

    @TestLogger.log('输入搜索关键字')
    def input_search_keyword(self, keyword):
        self.input_text(self.__locators['输入关键字搜索'], keyword)

    @TestLogger.log('清空搜索关键字')
    def clear_search_keyword(self):
        self.click_element(self.__locators['删除关键字'])

    @TestLogger.log('查看是否显示XX群')
    def is_group_in_list(self, name):
        time.sleep(2)
        locator = (MobileBy.ACCESSIBILITY_ID, "%s" % name)
        return self._is_element_present(locator)

    @TestLogger.log('点击群组')
    def click_group(self, name):
        self.click_element((MobileBy.XPATH, '//*[@resource-id="com.chinasofti.rcs:id/contact_name" and ' +
                            '@text="{}"]'.format(name)))