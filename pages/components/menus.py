from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger
from .dialogs import DeleteConfirmDialog


class LabelSettingMenu(DeleteConfirmDialog, BasePage):
    """标签设置"""
    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.LabelGroupSettingActivity'

    __locators = {
        '返回': (MobileBy.ACCESSIBILITY_ID, 'back'),
        '页面title': (MobileBy.ACCESSIBILITY_ID, '标签设置'),
        '标签名称': (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="标签名称"])[1]'),
        '移除成员': (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="移除成员"])[1]'),
        '删除标签': (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="删除标签"])[1]'),
        '修改标签名输入框': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField'),
        '修改名称页面确定按钮': (MobileBy.ACCESSIBILITY_ID, '确定'),
        '取消删除': (MobileBy.ACCESSIBILITY_ID, '取消'),
        '确认删除': (MobileBy.ACCESSIBILITY_ID, '删除'),
    }

    @TestLogger.log('点击返回')
    def click_back(self):
        self.click_element(self.__class__.__locators['返回'])

    @TestLogger.log('点击菜单：标签名称')
    def click_label_name_menu(self):
        self.click_element(self.__class__.__locators['标签名称'])

    @TestLogger.log('点击菜单：移除成员')
    def click_remove_member_menu(self):
        self.click_element(self.__class__.__locators['移除成员'])

    @TestLogger.log('点击菜单：删除标签')
    def click_delete_label_menu(self):
        self.click_element(self.__class__.__locators['删除标签'])

    @TestLogger.log('输入分组名字')
    def input_group_new_name(self, name):
        self.input_text(self.__class__.__locators['修改标签名输入框'], name)

    @TestLogger.log('点击修改分组名页面确定按钮')
    def click_confirm_modify(self):
        self.click_element(self.__class__.__locators['修改名称页面确定按钮'])

    @TestLogger.log('重命名标签')
    def rename_group_name(self, name):
        self.click_label_name_menu()
        self.input_group_new_name(name)
        self.click_confirm_modify()

    @TestLogger.log('移除成员')
    def remove_members(self, *members):
        from pages.components import ContactsSelector
        self.click_remove_member_menu()
        selector = ContactsSelector()
        selector.select_local_contacts(*members)

    @TestLogger.log('点击取消')
    def click_cancel(self):
        self.click_element(self.__locators['取消删除'])

    @TestLogger.log('点击删除')
    def click_delete(self):
        self.click_element(self.__locators['确认删除'])
