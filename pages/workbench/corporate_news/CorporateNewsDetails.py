from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger


class CorporateNewsDetailsPage(BasePage):
    """企业新闻详情页"""

    ACTIVITY = 'com.cmicc.module_enterprise.ui.activity.EnterpriseH5ProcessActivity'

    __locators = {
        '企业新闻详情': (MobileBy.IOS_PREDICATE, 'name=="企业新闻详情"'),
        '删除': (MobileBy.ACCESSIBILITY_ID, "删除"),
        '发布': (MobileBy.ACCESSIBILITY_ID, "发布"),
        '下线': (MobileBy.ACCESSIBILITY_ID, "下线"),
        '返回': (MobileBy.ID, 'com.chinasofti.rcs:id/btn_back_actionbar'),
        '确定': (MobileBy.IOS_PREDICATE, 'name=="确定"'),
        '取消': (MobileBy.XPATH, '//*[@text="取消"]'),
        '新闻详情页浏览量': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="企业新闻详情"]/XCUIElementTypeOther[3]/XCUIElementTypeStaticText'),
    }

    @TestLogger.log()
    def wait_for_page_load(self, timeout=20, auto_accept_alerts=True):
        """等待企业新闻详情页加载"""

        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["企业新闻详情"])
            )
        except:
            raise AssertionError("页面在{}s内，没有加载成功".format(str(timeout)))
        return self

    @TestLogger.log()
    def is_exist_delete_successfully(self):
        """是否存在删除成功"""
        return self.page_should_contain_text2("删除成功")

    @TestLogger.log()
    def is_exist_offline_successfully(self):
        """是否存在下线成功"""
        return self.page_should_contain_text2("下线成功")

    @TestLogger.log()
    def is_exist_release_successfully(self):
        """是否存在发布成功"""
        return self.page_should_contain_text2("发布成功")

    @TestLogger.log()
    def click_delete(self):
        """点击删除"""
        self.click_element(self.__class__.__locators["删除"])

    @TestLogger.log()
    def click_offline(self):
        """点击下线"""
        self.click_element(self.__class__.__locators["下线"])

    @TestLogger.log()
    def click_release(self):
        """点击发布"""
        self.click_element(self.__class__.__locators["发布"])

    @TestLogger.log()
    def click_back(self):
        """点击返回"""
        self.click_element(self.__class__.__locators["返回"])

    @TestLogger.log()
    def click_sure(self):
        """点击确定"""
        self.click_element(self.__class__.__locators["确定"])

    @TestLogger.log()
    def click_cancel(self):
        """点击取消"""
        self.click_element(self.__class__.__locators["取消"])

    @TestLogger.log()
    def get_corporate_news_detail_view(self):
        """返回某一条企业新闻详情页浏览量"""
        if self._is_element_present2(self.__class__.__locators["新闻详情页浏览量"]):
            el = self.get_element(self.__class__.__locators["新闻详情页浏览量"])
            amount = el.text
            return int(amount)