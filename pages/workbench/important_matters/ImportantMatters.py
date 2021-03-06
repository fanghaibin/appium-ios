from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger


class ImportantMattersPage(BasePage):
    """重要事项首页"""

    ACTIVITY = 'com.cmicc.module_enterprise.ui.activity.EnterpriseH5ProcessActivity'

    __locators = {
        '新建事项': (MobileBy.IOS_PREDICATE, 'name=="新建事项"'),
        '创建事项': (MobileBy.ACCESSIBILITY_ID, '创建事项'),
        '归档事项': (MobileBy.ACCESSIBILITY_ID, '归档事项'),
        '删除事项': (MobileBy.ACCESSIBILITY_ID, '删除事项'),
        '进行中的事项标题': (MobileBy.XPATH, '//*[contains(@name,"创建")]/../../XCUIElementTypeOther[1]/XCUIElementTypeStaticText'),
        '确定': (MobileBy.ACCESSIBILITY_ID, '确定'),
        '保存': (MobileBy.ACCESSIBILITY_ID, '保存'),
        '人员状态': (MobileBy.ACCESSIBILITY_ID, '人员状态'),
        '评论': (MobileBy.ACCESSIBILITY_ID, '评论'),
        '+子任务': (MobileBy.ACCESSIBILITY_ID, '+子任务'),
        '提交评论': (MobileBy.ACCESSIBILITY_ID, '提交评论'),
        '添加人员': (MobileBy.ACCESSIBILITY_ID, '添加人员'),
        '删除人员': (MobileBy.ACCESSIBILITY_ID, '删除人员'),
        '返回': (MobileBy.ID, 'com.chinasofti.rcs:id/btn_back_actionbar'),
        '关闭': (MobileBy.ID, 'com.chinasofti.rcs:id/btn_close_actionbar'),
        '创建事项页面标题输入框': (MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeTextField"'),
        '创建事项页面描述输入框': (MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeTextView"'),
        '查看事项页面标题输入框': (MobileBy.XPATH, '//*[@name="事项标题"]/../../following-sibling::*[1]/XCUIElementTypeStaticText'),
        '查看事项页面描述输入框': (MobileBy.XPATH, '//*[@name="事项描述"]/../../following-sibling::*[1]/XCUIElementTypeStaticText'),
        '事项修改编辑框': (MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeTextView"'),
        '+号': (MobileBy.XPATH, '//*[contains(@name,"参与人")]/../../following-sibling::*[1]/XCUIElementTypeOther[last()]/XCUIElementTypeOther[1]'),
        '事项标题栏三点': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="事项标题"]/../../following-sibling::*[2]'),
        '任务标题栏三点': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="任务标题"]/../../following-sibling::*[2]'),
        '子任务标题输入框': (MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeTextField"'),
        '子任务描述输入框': (MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeTextView"'),
        '子任务添加负责人+号': (MobileBy.XPATH, '//*[contains(@name,"负责人")]/../../following-sibling::*[1]/XCUIElementTypeOther/XCUIElementTypeOther'),
        '修改': (MobileBy.ACCESSIBILITY_ID, '修改'),
        '查看子任务': (MobileBy.IOS_PREDICATE, 'name=="查看子任务"'),
        '删除子任务': (MobileBy.ACCESSIBILITY_ID, '删除子任务'),
        '查看进行中的事项': (MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeLink" and name=="查看进行中的事项"'),
        '查看已归档的事项': (MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeLink" and name=="查看已归档的事项"'),
    }

    @TestLogger.log()
    def wait_for_page_load(self, timeout=60, auto_accept_alerts=True):
        """等待重要事项首页加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["新建事项"])
            )
        except:
            raise AssertionError("页面在{}s内，没有加载成功".format(str(timeout)))
        return self

    @TestLogger.log()
    def is_on_important_matters_page(self, timeout=20, auto_accept_alerts=True):
        """当前页面是否在重要事项首页"""

        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["新建事项"])
            )
            return True
        except:
            return False

    @TestLogger.log()
    def click_back(self):
        """点击返回"""
        self.click_element(self.__class__.__locators["返回"])

    @TestLogger.log()
    def click_close(self):
        """点击关闭"""
        self.click_element(self.__class__.__locators["关闭"])

    @TestLogger.log()
    def click_new_item(self):
        """点击新建事项"""
        self.click_element(self.__class__.__locators["新建事项"])

    @TestLogger.log()
    def click_create_item(self):
        """点击创建事项"""
        self.click_element(self.__class__.__locators["创建事项"])

    @TestLogger.log()
    def wait_for_create_item_page_load(self, timeout=30, auto_accept_alerts=True):
        """等待创建事项页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["创建事项"])
            )
        except:
            raise AssertionError("页面在{}s内，没有加载成功".format(str(timeout)))
        return self

    @TestLogger.log()
    def wait_for_check_item_page_load(self, timeout=30, auto_accept_alerts=True):
        """等待查看事项页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["归档事项"])
            )
        except:
            raise AssertionError("页面在{}s内，没有加载成功".format(str(timeout)))
        return self

    @TestLogger.log()
    def wait_for_personnel_status_page_load(self, timeout=30, auto_accept_alerts=True):
        """等待人员状态页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["添加人员"])
            )
        except:
            raise AssertionError("页面在{}s内，没有加载成功".format(str(timeout)))
        return self

    @TestLogger.log()
    def input_create_item_title(self, title):
        """输入创建事项页面标题"""
        self.input_text(self.__class__.__locators["创建事项页面标题输入框"], title)

    @TestLogger.log()
    def input_create_item_describe(self, describe):
        """输入创建事项页面描述"""
        self.input_text(self.__class__.__locators["创建事项页面描述输入框"], describe)

    @TestLogger.log()
    def input_modify_content(self, content):
        """输入修改内容"""
        self.input_text(self.__class__.__locators["事项修改编辑框"], content)

    @TestLogger.log()
    def click_check_item_title(self):
        """点击查看事项页面标题"""
        self.click_element(self.__class__.__locators["查看事项页面标题输入框"])

    @TestLogger.log()
    def click_check_item_describe(self):
        """点击查看事项页面描述"""
        self.click_element(self.__class__.__locators["查看事项页面描述输入框"])

    @TestLogger.log()
    def click_add_icon(self):
        """点击+号"""
        self.click_coordinates(self.__class__.__locators["+号"])

    @TestLogger.log()
    def click_three_points_icon(self):
        """点击事项标题栏右侧三点"""
        self.click_coordinates(self.__class__.__locators["事项标题栏三点"])

    @TestLogger.log()
    def click_task_three_points_icon(self):
        """点击任务标题栏右侧三点"""
        self.click_coordinates(self.__class__.__locators["任务标题栏三点"])

    @TestLogger.log()
    def click_delete_item(self):
        """点击删除事项"""
        self.click_element(self.__class__.__locators["删除事项"])

    @TestLogger.log()
    def click_sure(self):
        """点击确定"""
        self.click_element(self.__class__.__locators["确定"])

    @TestLogger.log()
    def click_save(self):
        """点击保存"""
        self.click_element(self.__class__.__locators["保存"])

    @TestLogger.log()
    def click_personnel_status(self):
        """点击人员状态"""
        self.click_element(self.__class__.__locators["人员状态"])

    @TestLogger.log()
    def click_comment(self):
        """点击评论"""
        self.click_element(self.__class__.__locators["评论"])

    @TestLogger.log()
    def click_submit_comments(self):
        """点击提交评论"""
        self.click_element(self.__class__.__locators["提交评论"])

    @TestLogger.log()
    def click_add_personnel(self):
        """点击添加人员"""
        self.click_element(self.__class__.__locators["添加人员"])

    @TestLogger.log()
    def click_delete_personnel(self):
        """点击删除人员"""
        self.click_element(self.__class__.__locators["删除人员"])

    @TestLogger.log()
    def click_first_item(self):
        """点击第一条进行中的事项"""
        self.click_element(self.__class__.__locators["进行中的事项标题"])

    @TestLogger.log()
    def is_exists_item(self):
        """是否存在已有事项"""
        return self._is_element_present2(self.__class__.__locators["进行中的事项标题"])

    @TestLogger.log()
    def is_exists_delete_icon_by_name(self, name):
        """是否存在指定联系人删除图标"""
        locator = (MobileBy.XPATH, '//*[@name="%s"]/../following-sibling::*[count(*)=0]' % name)
        return self._is_element_present2(locator)

    @TestLogger.log()
    def click_delete_icon_by_name(self, name):
        """点击指定联系人删除图标"""
        locator = (MobileBy.XPATH, '//*[@name="%s"]/../following-sibling::*[1]' % name)
        self.click_coordinates(locator)

    @TestLogger.log()
    def click_delete_icon_by_comment(self, comment):
        """点击指定评论删除图标"""
        locator = (MobileBy.XPATH, '//*[contains(@name,"%s")]/../following-sibling::*[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[@name="删除"]' % comment)
        self.click_element(locator)

    @TestLogger.log()
    def clear_item(self):
        """清空进行中的事项"""
        current = 0
        while self._is_element_present2(self.__class__.__locators["进行中的事项标题"]):
            current += 1
            if current > 20:
                return
            el = self.get_element(self.__class__.__locators["进行中的事项标题"])
            el.click()
            self.wait_for_check_item_page_load()
            self.click_three_points_icon()
            self.click_delete_item()
            self.click_sure()
            self.wait_for_page_load()

    @TestLogger.log()
    def wait_for_filed_list_page_load(self, timeout=30, auto_accept_alerts=True):
        """等待已归档事项列表加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["查看进行中的事项"])
            )
        except:
            raise AssertionError("页面在{}s内，没有加载成功".format(str(timeout)))
        return self

    @TestLogger.log()
    def click_check_having_item(self):
        """点击查看进行中的事项"""
        self.click_element(self.__class__.__locators["查看进行中的事项"])

    @TestLogger.log()
    def click_filed_item(self):
        """点击查看已归档的事项"""
        self.click_element(self.__class__.__locators["查看已归档的事项"])

    @TestLogger.log()
    def wait_for_add_subtasks_page_load(self, timeout=30, auto_accept_alerts=True):
        """等待添加子任务页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["保存"])
            )
        except:
            raise AssertionError("页面在{}s内，没有加载成功".format(str(timeout)))
        return self

    @TestLogger.log()
    def wait_for_check_subtasks_page_load(self, timeout=30, auto_accept_alerts=True):
        """等待查看子任务页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["查看子任务"])
            )
        except:
            raise AssertionError("页面在{}s内，没有加载成功".format(str(timeout)))
        return self

    @TestLogger.log()
    def input_subtasks_title(self, title):
        """输入子任务标题"""
        self.input_text(self.__class__.__locators["子任务标题输入框"], title)

    @TestLogger.log()
    def input_subtasks_describe(self, describe):
        """输入子任务描述"""
        self.input_text(self.__class__.__locators["子任务描述输入框"], describe)

    @TestLogger.log()
    def click_subtasks_add_icon(self):
        """点击子任务页面+号"""
        self.click_coordinates(self.__class__.__locators["子任务添加负责人+号"])

    @TestLogger.log()
    def click_delete_subtasks(self):
        """点击删除子任务"""
        self.click_element(self.__class__.__locators["删除子任务"])

    @TestLogger.log()
    def click_add_subtasks(self):
        """点击+子任务"""
        self.click_element(self.__class__.__locators["+子任务"])

    @TestLogger.log()
    def swipe_time_by_year(self):
        """滑动子任务截止时间-年"""
        self.swipe_by_percent_on_screen(10.14, 92.4, 10.14, 82.6)

    @TestLogger.log()
    def swipe_time_by_month(self):
        """滑动子任务截止时间-月"""
        self.swipe_by_percent_on_screen(30.4, 92.4, 30.4, 82.6)

    @TestLogger.log()
    def swipe_time_by_day(self):
        """滑动子任务截止时间-日"""
        self.swipe_by_percent_on_screen(49.76, 92.4, 49.76, 82.6)

    @TestLogger.log()
    def swipe_time_by_hour(self):
        """滑动子任务截止时间-时"""
        self.swipe_by_percent_on_screen(70.05, 92.4, 70.05, 82.6)

    @TestLogger.log()
    def swipe_time_by_minute(self):
        """滑动子任务截止时间-分"""
        self.swipe_by_percent_on_screen(89.37, 95, 89.37, 80)

    @TestLogger.log()
    def click_year(self, text):
        """选择年份"""
        locator = (MobileBy.ACCESSIBILITY_ID, "%s" % text)
        if self._is_element_present2(locator):
            n = 10
            while n:
                try:
                    self.mobile.click_element(locator)
                    return
                except:
                    self.swipe_time_by_year()
                    self.click_coordinate(100, 100)
                    n -= 1

    @TestLogger.log()
    def click_hour(self, text):
        """选择时"""
        locator = (MobileBy.ACCESSIBILITY_ID, "%s时" % text)
        if self._is_element_present2(locator):
            n = 10
            while n:
                try:
                    self.mobile.click_element(locator)
                    return
                except:
                    self.swipe_time_by_hour()
                    self.click_coordinate(100, 100)
                    n -= 1

    @TestLogger.log()
    def click_minute(self, text):
        """选择分"""
        locator = (MobileBy.ACCESSIBILITY_ID, "%s分" % text)
        if self._is_element_present2(locator):
            n = 30
            while n:
                try:
                    self.mobile.click_element(locator)
                    return
                except:
                    self.swipe_time_by_minute()
                    self.click_coordinate(100, 100)
                    n -= 1

    @TestLogger.log()
    def click_modify(self):
        """点击修改"""
        self.click_element(self.__class__.__locators["修改"])

    @TestLogger.log()
    def click_file_matters(self):
        """点击归档事项"""
        self.click_element(self.__class__.__locators["归档事项"])
