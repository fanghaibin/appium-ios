from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger
import time

class MultiPartyVideoPage(BasePage):
    """多方视频页面"""
    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.ContactSelectorActivity'

    __locators = {
        '返回': (MobileBy.ID, 'back'),
        'com.chinasofti.rcs:id/action_bar_root': (MobileBy.ID, 'com.chinasofti.rcs:id/action_bar_root'),
        'android:id/content': (MobileBy.ID, 'android:id/content'),
        'com.chinasofti.rcs:id/id_toolbar': (MobileBy.ID, 'com.chinasofti.rcs:id/id_toolbar'),
        'com.chinasofti.rcs:id/back': (MobileBy.ID, 'com.chinasofti.rcs:id/back'),
        '多方视频': (MobileBy.ID, 'com.chinasofti.rcs:id/title'),
        '呼叫': (MobileBy.XPATH, "//*[@type='XCUIElementTypeButton']"),
        '灰色呼叫': (MobileBy.ID, '呼叫'),
        '搜索或输入号码': (MobileBy.ID, '搜索或输入号码'),
        '搜索群成员': (MobileBy.ID, '搜索群成员'),
        'com.chinasofti.rcs:id/contentFrame': (MobileBy.ID, 'com.chinasofti.rcs:id/contentFrame'),
        'com.chinasofti.rcs:id/local_contact_lv': (MobileBy.ID, 'com.chinasofti.rcs:id/local_contact_lv'),
        'com.chinasofti.rcs:id/contact_list': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_list'),
        'com.chinasofti.rcs:id/local_contacts': (MobileBy.ID, 'com.chinasofti.rcs:id/local_contacts'),
        '选择和通讯录联系人': (MobileBy.ID, 'com.chinasofti.rcs:id/text_hint'),
        'com.chinasofti.rcs:id/arrow_right': (MobileBy.ID, 'com.chinasofti.rcs:id/arrow_right'),
        '联系人item': (MobileBy.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell"),
        'D': (MobileBy.ID, 'com.chinasofti.rcs:id/index_text'),
        '头像': (MobileBy.ID, 'com.chinasofti.rcs:id/head_tv'),
        '联系人头像': (MobileBy.XPATH, "//*[@type='XCUIElementTypeImage']"),
        '大佬1': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_name'),
        '联系人号码': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_number'),
        '大佬2': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_name'),
        '13800138006': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_number'),
        '大佬3': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_name'),
        '13800138007': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_number'),
        '大佬4': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_name'),
        '13800138008': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_number'),
        'G': (MobileBy.ID, 'com.chinasofti.rcs:id/index_text'),
        '给个红包1': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_name'),
        '13800138000': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_number'),
        '给个红包2': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_name'),
        '13800138001': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_number'),
        '给个红包3': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_name'),
        '已选择成员': (MobileBy.ID, 'com.chinasofti.rcs:id/hor_contact_selection'),
        '挂断多方视频': (MobileBy.ID, 'com.chinasofti.rcs:id/end_video_call_btn'),
        '确定': (MobileBy.XPATH, '//*[@label="确定"]'),
        '取消': (MobileBy.ID, 'com.chinasofti.rcs:id/btn_cancel'),
        '再次呼叫': (MobileBy.XPATH, '//*[@label="再次呼叫"]'),
        '一键建群': (MobileBy.ID, '一键建群'),
        '团队联系人图像': (MobileBy.XPATH, '//*[@type="XCUIElementTypeStaticText"]'),
        '红色挂断按钮': (MobileBy.IOS_PREDICATE, 'name contains "cc call ipcall red normal"'),
        '关闭摄像头': (MobileBy.ID, '关闭摄像头'),
        '免提': (MobileBy.ID, '免提'),
        '静音': (MobileBy.ID, '静音'),
        '添加成员': (MobileBy.ID, 'cc chat message site normal'),
        '呼叫按钮': (MobileBy.IOS_PREDICATE, 'name == "呼叫"'),
    }

    @TestLogger.log()
    def click_contact_head(self, index=0):
        """点击联系人头像"""
        el = self.get_elements(self.__locators["头像"])
        el[index].click()

    @TestLogger.log()
    def is_exist_contact_head(self):
        """是否存在搜索结果"""
        return self._is_element_present(self.__locators["头像"])

    @TestLogger.log()
    def is_on_multi_party_video_page(self):
        """判断当前是否在多方视频选择界面"""
        return self._is_element_present(self.__locators["多方视频"])

    @TestLogger.log()
    def is_exist_contact_selection(self):
        """判断当前是否存在已选择成员"""
        return self._is_element_present(self.__locators["已选择成员"])

    @TestLogger.log()
    def click_call(self):
        """点击呼叫"""
        self.click_element(self.__locators["呼叫"])

    @TestLogger.log()
    def click_tv_sure(self):
        """点击呼叫"""
        self.click_element(self.__locators["呼叫"])


    @TestLogger.log()
    def input_contact_search(self, text):
        """输入电话号码并搜索"""
        self.input_text(self.__locators["搜索或输入号码"], text)

    @TestLogger.log()
    def input_group_number_search(self, text):
        """搜索群成员"""
        self.input_text(self.__locators["搜索群成员"], text)

    @TestLogger.log()
    def click_end_video_call(self):
        """点击挂断多方通话"""
        self.click_element(self.__locators["挂断多方视频"])

    @TestLogger.log()
    def is_exist_end_video_call(self):
        """判断当前是否存在挂断多方通话"""
        return self._is_element_present(self.__locators["挂断多方视频"])

    @TestLogger.log()
    def click_btn_ok(self):
        """点击确定"""
        self.click_element(self.__locators["确定"])

    @TestLogger.log()
    def click_call_again(self):
        """点击再次呼叫"""
        self.click_element(self.__locators["再次呼叫"])

    @TestLogger.log()
    def click_one_key_new_group(self):
        """点击一键建群"""
        self.click_element(self.__locators["一键建群"])

    @TestLogger.log()
    def click_contact_icon(self, index=0):
        """点击联系人头像"""
        el = self.get_elements(self.__locators["联系人头像"])
        try:
            if len(el) > 0:
                el[index].click()
        except:
            raise IndexError("元素超出索引")

    @TestLogger.log()
    def select_contacts_by_number(self, number):
        """根据号码选择一个联系人"""
        time.sleep(1)
        locator = (MobileBy.XPATH, '//*[contains(@name,"%s")]' % number)
        max_try = 20
        current = 0
        while current < max_try:

            if self._is_element_present(locator):
                break
            self.swipe_by_percent_on_screen(50, 70, 50, 30, 700)
            current += 1
        self.click_element(locator)

    @TestLogger.log()
    def select_contacts_by_name(self, name):
        """根据号码选择一个联系人"""
        time.sleep(1)
        locator = (MobileBy.XPATH, '//*[@resource-id="com.chinasofti.rcs:id/contact_name" and @text ="%s"]' % name)
        max_try = 20
        current = 0
        while current < max_try:

            if self._is_element_present(locator):
                break
            self.swipe_by_percent_on_screen(50, 70, 50, 30, 700)
            current += 1
        self.click_element(locator)

    def click_select_contacts(self, index):
        """通过下标点击选择联系人"""
        elements = self.get_elements(self.__locators["联系人号码"])
        try:
            if len(elements) > 0:
                return elements[index].click()
        except:
            raise IndexError("元素超出索引")

    @TestLogger.log()
    def is_exist_back_button(self):
        """判断当前是否存在返回按钮"""
        return self._is_element_present(self.__locators["返回"])

    @TestLogger.log()
    def is_enabled_tv_sure(self):
        """判断呼叫按钮是否可用"""
        return self._is_enabled(self.__locators["灰色呼叫"])

    @TestLogger.log()
    def get_contactlist_index(self, name):
        """获取团队联系人的下表"""
        elements = self.get_elements(self.__locators["团队联系人图像"])
        lst = []
        try:
            if len(elements) > 0:
                for i in range(len(elements)):
                    lst.append(elements[i].text)
        except:
            raise IndexError("元素超出索引")
        for item in lst:
            if name == item:
                return lst.index(name)

    @TestLogger.log()
    def click_img_icon_contactlist(self):
        """点击团队联系人图像"""
        self.click_element(self.__locators["团队联系人图像"])

    @TestLogger.log()
    def sure_button_is_enabled(self):
        """确定呼叫是否可点击"""
        return self._is_enabled(self.__class__.__locators["呼叫"])

    @TestLogger.log()
    def click_contact_list_item(self, index):
        """点击联系人"""
        el = self.get_elements(self.__locators["联系人item"])
        try:
            if len(el) > 0:
                el[index].click()
        except:
            raise IndexError("元素超出索引")

    @TestLogger.log()
    def wait_until_not_video_call_page(self, timeout=60, auto_accept_alerts=True):
        """等待视频通话界面消失"""
        try:
            self.wait_until_not(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self.is_text_present("关闭摄像头")
            )
        except:
            raise AssertionError("通话界面未显示")
        return self

    @TestLogger.log()
    def click_element_by_text(self, text):
        """点击指定元素"""
        self.click_element(self.__class__.__locators[text])

    @TestLogger.log()
    def is_exists_element_by_text(self, text):
        """是否存在指定元素"""
        return self._is_element_present2(self.__class__.__locators[text])

    @TestLogger.log()
    def click_close_camera(self):
        """点击关闭摄像头"""
        self.click_element(self.__locators["关闭摄像头"])

    @TestLogger.log()
    def click_hands_free(self):
        """点击免提"""
        self.click_element(self.__locators["免提"])

    @TestLogger.log()
    def click_mute(self):
        """点击静音"""
        self.click_element(self.__locators["静音"])

    @TestLogger.log()
    def click_red_drop(self):
        """点击红色挂断按钮"""
        self.click_element(self.__locators["红色挂断按钮"])

    @TestLogger.log()
    def click_add_members(self):
        """点击添加成员按钮"""
        self.click_element(self.__locators["添加成员"])

    @TestLogger.log()
    def _is_enabled_call_button(self):
        """呼叫按钮是否可点击"""
        return self._is_enabled(self.__class__.__locators["呼叫按钮"])

