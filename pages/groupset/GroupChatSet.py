from appium.webdriver.common.mobileby import MobileBy
import re
from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger
import time

class GroupChatSetPage(BasePage):
    """群聊设置页面"""
    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.GroupSettingActivity'

    __locators = {
        '返回': (MobileBy.ACCESSIBILITY_ID, 'back'),
        '群成员列表入口': (MobileBy.IOS_PREDICATE, 'name CONTAINS "群成员"'),
        '添加成员': (MobileBy.IOS_PREDICATE, 'name CONTAINS "cc_chat_groupchat_add_normal"'),
        '删除成员': (MobileBy.IOS_PREDICATE, 'name CONTAINS "cc_chat_groupchat_delete_normal"'),
        '皇冠标志': (MobileBy.IOS_PREDICATE, 'name CONTAINS "chat_group_crown"'),
        '邀请微信或QQ好友进群': (MobileBy.IOS_PREDICATE, 'name == "邀请微信或QQ好友进群"'),
        '群名称': (MobileBy.ACCESSIBILITY_ID, '群名称'),
        '我的群昵称': (MobileBy.ACCESSIBILITY_ID, '我的群昵称'),
        '群二维码': (MobileBy.IOS_PREDICATE, 'name == "群二维码"'),
        '小键盘麦克标志': (MobileBy.IOS_PREDICATE, 'name == "dictation"'),
        '二维码': (MobileBy.ACCESSIBILITY_ID, 'cc_chat_groupsetting_qrcode.png'),
        '群管理1': (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="群管理"])[1]'),
        '查找聊天内容': (MobileBy.IOS_PREDICATE, 'name == "查找聊天内容"'),
        '群消息免打扰开关': (MobileBy.XPATH, '//XCUIElementTypeSwitch[@name="群消息免打扰"]'),
        '置顶聊天开关': (MobileBy.XPATH, '//XCUIElementTypeSwitch[@name="置顶聊天"]'),
        '删除并退出': (MobileBy.ACCESSIBILITY_ID, '删除并退出'),
        '退出': (MobileBy.ACCESSIBILITY_ID, '退出'),
        # 退出企业群弹框
        '取消': (MobileBy.ACCESSIBILITY_ID, '取消'),
        '转让': (MobileBy.ACCESSIBILITY_ID, '转让'),
        '确定': (MobileBy.IOS_PREDICATE, 'name CONTAINS "确定"'),
        # 移除成员页面
        '成员列表-排列第一的成员': (MobileBy.XPATH,
                         '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]'),
        '弹框-确定': (MobileBy.XPATH, '(//*[contains(@name,"确定")])[2]'),
        # 查找聊天内容页面
        '输入关键字快速搜索': (MobileBy.IOS_PREDICATE, 'value == "输入关键字快速搜索"'),
        '搜索结果排列第一项': (MobileBy.XPATH,
                      '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable[2]/XCUIElementTypeCell'),
        # 群成员列表页面
        '搜索群成员': (MobileBy.IOS_PREDICATE, 'name == "搜索群成员"'),
        '未开通': (MobileBy.ACCESSIBILITY_ID, '未开通'),
        '邀请': (MobileBy.ACCESSIBILITY_ID, '邀请'),
        '搜索群成员结果': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="搜索结果"]/XCUIElementTypeCell'),
        '菜单区域': (MobileBy.CLASS_NAME, 'android.widget.ScrollView'),
        '群聊设置': (MobileBy.ACCESSIBILITY_ID, '群聊设置'),
        '群成员列表': (MobileBy.XPATH, '//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell'),
        # 编辑群名称页面
        '请输入群聊名称': (MobileBy.IOS_PREDICATE, 'value CONTAINS "请输入群聊名称"'),
        '完成': (MobileBy.ACCESSIBILITY_ID, '完成'),
        'com.chinasofti.rcs:id/show_more_member': (MobileBy.ID, 'com.chinasofti.rcs:id/show_more_member'),
        '群成员(2人)': (MobileBy.ID, 'com.chinasofti.rcs:id/member_count'),
        '群成员展开>': (
            MobileBy.XPATH,
            '//*[@resource-id="com.chinasofti.rcs:id/member_count"]/../android.widget.ImageView'),
        '群聊名称': (MobileBy.ID, 'com.chinasofti.rcs:id/left_group_chat_name_tv'),
        '群聊001': (MobileBy.ID, 'com.chinasofti.rcs:id/group_name'),
        '修改群聊名称': (MobileBy.ID, 'com.chinasofti.rcs:id/group_name_right_arrow'),
        '我在本群的昵称': (MobileBy.XPATH, '//*[@name="我的群昵称"]/following-sibling::XCUIElementTypeStaticText[1]'),
        "确认": (MobileBy.XPATH, '//*[@text ="确认"]'),
        '修改群名或群名片返回': (MobileBy.ID, 'com.chinasofti.rcs:id/back'),
        'X按钮': (MobileBy.ID, 'com.chinasofti.rcs:id/iv_delect'),
        '群名片完成': (MobileBy.ID, 'com.chinasofti.rcs:id/group_card_save'),
        '二维码转发': (MobileBy.IOS_PREDICATE, 'name CONTAINS "cc me qrcode share normal"'),
        '二维码保存': (MobileBy.IOS_PREDICATE, 'name CONTAINS "cc me qrcode save normal"'),
        '二维码返回': (MobileBy.ID, 'com.chinasofti.rcs:id/left_back'),
        '群管理返回': (MobileBy.ID, 'com.chinasofti.rcs:id/back'),
        '群主管理权转让': (MobileBy.IOS_PREDICATE, 'name == "群主管理权转让"'),
        '解散群': (MobileBy.IOS_PREDICATE, 'name == "解散群"'),
        '解散': (MobileBy.IOS_PREDICATE, 'name == "解散"'),
        # 邀请分享群口令
        '分享群口令框': (MobileBy.XPATH, '//*[@text ="分享群口令邀请好友进群"]'),
        '下次再说': (MobileBy.IOS_PREDICATE, 'name == "下次再说"'),
        '立即分享': (MobileBy.IOS_PREDICATE, 'name == "立即分享"'),
        "再次邀请": (MobileBy.IOS_PREDICATE, 'name CONTAINS "还有人未进群"'),
        "再次邀请按钮": (MobileBy.ACCESSIBILITY_ID, '一键邀请'),
        '微信': (MobileBy.IOS_PREDICATE, 'name == "微信"'),
        'QQ': (MobileBy.IOS_PREDICATE, 'name == "QQ"'),
        '取消按钮': (MobileBy.IOS_PREDICATE, 'name == "取消"'),
        '群管理': (MobileBy.IOS_PREDICATE, 'name == "群管理"'),
        '空列表': (MobileBy.IOS_PREDICATE, 'name == "空列表"'),
        '清除文本': (MobileBy.IOS_PREDICATE, 'name == "清除文本"'),
        '群成员文本': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeStaticText[1]'),
        '群成员头像': (MobileBy.XPATH,
                  '//*[contains(@name,"cc_chat_groupchat_add_normal")]/../../../preceding-sibling::XCUIElementTypeCell[*]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage'),
        '群成员名字': (MobileBy.XPATH,
                  '//*[contains(@name,"cc_chat_groupchat_add_normal")]/../../../preceding-sibling::XCUIElementTypeCell[*]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText'),
        '群主头像皇冠': (MobileBy.XPATH,
                   '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage[contains(@name,"chat_group_crown")]'),
        '群成员搜索框': (MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeSearchField"'),
    }

    @TestLogger.log()
    def click_edit_group_name(self):
        """点击编辑群名称"""
        self.click_element(self.__class__.__locators['群名称'])

    @TestLogger.log()
    def click_invite_to_use_again_someone_notuse(self):
        """点击再次邀请(无法用元素定位，使用坐标定位)"""
        # self.click_element(self.__class__.__locators['再次邀请'])
        self.click_coordinate(61, 20)


    @TestLogger.log()
    def click_invite_to_use_again(self):
        """点击再次邀请"""
        self.click_element(self.__class__.__locators['再次邀请按钮'])


    @TestLogger.log()
    def click_clear_group_name(self):
        """点击清除群名称"""
        self.click_element(self.__class__.__locators['清除文本'])

    @TestLogger.log()
    def input_new_group_name(self, name):
        """输入新的群名称"""
        self.input_text(self.__class__.__locators['请输入群聊名称'], name)

    @TestLogger.log()
    def save_group_name(self):
        """保存新群名"""
        self.click_element(self.__class__.__locators['完成'])

    @TestLogger.log()
    def change_group_name(self, name):
        """修改新的群聊"""
        self.click_edit_group_name()
        self.click_clear_group_name()
        self.input_new_group_name(name)
        self.save_group_name()
        time.sleep(3)

    @TestLogger.log()
    def change_my_name_in_group(self, name):
        """修改我在群聊中的名称"""
        self.click_my_card()
        self.click_clear_group_name()
        self.input_text((MobileBy.IOS_PREDICATE, 'value == "设置您在群内显示的昵称"'), name)
        self.save_group_name()
        time.sleep(3)



    @TestLogger.log()
    def click_save_code(self):
        """点击保存群二维码"""
        self.click_element(self.__class__.__locators["二维码保存"])

    @TestLogger.log()
    def is_exist_crown(self):
        """是否小皇冠标志"""
        return self._is_element_present(self.__class__.__locators["皇冠标志"])

    def is_exist_msg_dictation(self):
        """当前页面是否有小键盘麦克"""
        el = self.get_elements(self.__locators['小键盘麦克标志'])
        return len(el) > 0

    @TestLogger.log()
    def is_exist_code_forward_button(self):
        """是否存在二维码转发按钮"""
        return self._is_element_present(self.__class__.__locators["二维码转发"])

    @TestLogger.log()
    def click_group_code(self):
        """点击群二维码按钮"""
        self.click_element(self.__class__.__locators["群二维码"])

    @TestLogger.log()
    def click_find_message_records(self):
        """点击查找聊天内容"""
        self.click_element(self.__class__.__locators["查找聊天内容"])

    @TestLogger.log()
    def click_code_forward(self):
        """点击二维码转发按钮"""
        self.click_element(self.__class__.__locators["二维码转发"])

    @TestLogger.log()
    def click_clear_text(self):
        """点击清除文本按钮"""
        self.click_element(self.__class__.__locators["清除文本"])

    @TestLogger.log()
    def is_exist_empty_list(self):
        """是否存在空列表"""
        return self._is_element_present(self.__class__.__locators["空列表"])

    @TestLogger.log()
    def click_group_control(self):
        """点击群管理按钮"""
        self.click_element(self.__class__.__locators["群管理"])

    @TestLogger.log()
    def dissolution_the_group(self, times=2):
        """解散群"""
        self.click_group_control()
        self.click_group_manage_disband_button()
        self.click_sure_disband_button()
        time.sleep(times)
        from pages import GroupChatPage
        GroupChatPage().click_back()

    @TestLogger.log()
    def is_exist_cancel_button(self):
        """是否存在取消按钮"""
        return self._is_element_present(self.__class__.__locators["取消按钮"])

    @TestLogger.log()
    def click_share_wechat(self):
        """点击分享到微信"""
        self.click_element(self.__locators['微信'])

    @TestLogger.log()
    def click_share_qq(self):
        """点击立即分享"""
        self.click_element(self.__locators['QQ'])

    @TestLogger.log()
    def click_sharing(self):
        """点击立即分享"""
        self.click_element(self.__locators['立即分享'])

    @TestLogger.log()
    def click_next_time(self):
        """点击下次再说"""
        self.click_element(self.__locators['下次再说'])

    @TestLogger.log()
    def click_invite_friend(self):
        """点击邀请微信或QQ好友进群"""
        self.click_element(self.__locators['邀请微信或QQ好友进群'])

    @TestLogger.log()
    def is_on_this_page(self):
        """当前页面是否在通讯录"""

        try:
            self.wait_until(
                timeout=15,
                auto_accept_permission_alert=True,
                condition=lambda d: self.is_text_present('群聊设置')
            )
            return True
        except:
            return False

    @TestLogger.log()
    def click_switch_undisturb(self):
        """点击消息免打扰开关"""
        self.click_element(self.__class__.__locators['群消息免打扰开关'])

    @TestLogger.log()
    def get_switch_undisturb_value(self):
        """获取免打扰开关的值"""
        time.sleep(2)
        if self._is_element_present2(self.__class__.__locators["群消息免打扰开关"]):
            el = self.get_element(self.__class__.__locators["群消息免打扰开关"])
            return el.text

    @TestLogger.log()
    def click_switch_top(self):
        """点击置顶聊天开关"""
        self.click_element(self.__class__.__locators['置顶聊天开关'])

    @TestLogger.log()
    def get_switch_top_value(self):
        """获取置顶聊天开关的值"""
        if self._is_element_present2(self.__class__.__locators["置顶聊天开关"]):
            el = self.get_element(self.__class__.__locators["置顶聊天开关"])
            return el.text

    @TestLogger.log('点击返回')
    def click_back(self):
        self.click_element(self.__locators['返回'])

    @TestLogger.log()
    def wait_for_page_load(self, timeout=60, auto_accept_alerts=True):
        """等待群聊设置页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["群聊设置"])
            )
        except:
            message = "页面在{}s内，没有加载成功".format(str(timeout))
            raise AssertionError(
                message
            )
        return self

    @TestLogger.log()
    def click_add_member(self):
        """点击 '+ ': 添加成员"""
        self.click_element(self.__class__.__locators['添加成员'])

    @TestLogger.log()
    def click_enter_contact_list(self):
        """点击进入群成员列表"""
        self.click_element(self.__class__.__locators['群成员列表入口'])

    @TestLogger.log()
    def click_search_group_contact(self):
        """点击搜索群成员"""
        self.click_element(self.__class__.__locators['搜索群成员'])

    @TestLogger.log()
    def input_contact_name(self, text):
        """搜索群成员页面-输入搜索文本"""
        self.input_text(self.__class__.__locators['搜索群成员'], text)

    @TestLogger.log()
    def click_search_group_contact_result(self):
        """点击搜索群成员结果列表"""
        self.click_element(self.__class__.__locators['搜索群成员结果'])

    @TestLogger.log()
    def click_del_member(self):
        """点击 '-': 删除成员"""
        self.click_element(self.__class__.__locators['删除成员'])

    @TestLogger.log()
    def is_exit_element(self, locator='消息列表1'):
        """是否存在某元素"""
        return self._is_element_present(self.__class__.__locators[locator])

    @TestLogger.log()
    def click_delete_and_exit(self):
        """点击删除并退出"""
        self.click_element(self.__locators['删除并退出'])

    @TestLogger.log()
    def click_transfer_of_group(self):
        """点击转让群组"""
        self.click_element(self.__locators['转让'])
        time.sleep(3)

    @TestLogger.log('通过名字选择联系人')
    def select_contact_by_name(self, name='大佬1'):
        locator = (MobileBy.ACCESSIBILITY_ID, '%s' % name)
        self.click_element(locator)

    @TestLogger.log()
    def exit_enterprise_group(self, text='大佬2'):
        """退出企业群"""
        self.click_delete_and_exit()
        if self.is_exit_element(locator='转让'):
            # 群人数大于3人时,需要转让群主
            self.click_transfer_of_group()
            time.sleep(2)
            self.select_contact_by_name(name=text)
            time.sleep(4)
        else:
            # 群人数小于3人,可直接退出
            self.click_sure_exit_group()
            time.sleep(2)

    @TestLogger.log()
    def click_cancel(self):
        """点击取消"""
        self.click_element(self.__locators['取消'])

    @TestLogger.log()
    def click_sure(self):
        """点击确定"""
        self.click_element(self.__locators['确定'])

    @TestLogger.log()
    def click_sure_icon(self):
        """点击确定按钮（弹出框确定）"""
        self.click_element(self.__locators['弹框-确定'])

    @TestLogger.log()
    def click_menber_list_first_member(self):
        """点击成员列表排列第一的成员"""

        self.click_element(self.__locators['成员列表-排列第一的成员'])

    @TestLogger.log()
    def click_input_box(self):
        """查找聊天内容页面-输入关键字快速搜索"""
        self.click_element(self.__class__.__locators['输入关键字快速搜索'])

    @TestLogger.log()
    def input_search_keyword(self,text):
        """查找聊天内容页面-输入搜索文本"""
        self.input_text(self.__class__.__locators['输入关键字快速搜索'], text)

    @TestLogger.log()
    def click_search_result_first_list(self):
        """查找聊天内容页面-点击搜索结果排列第一的项"""
        locator = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable[2]/XCUIElementTypeCell')
        els = self.get_elements(locator)
        time.sleep(2)
        els[0].click()

    @TestLogger.log()
    def get_group_members_number(self):
        """获取群人数"""
        locator = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
        els = self.get_elements(locator)
        # print(els)
        return len(els[:-2])

    @TestLogger.log()
    def get_first_number_name(self):
        """获取第一个群聊成员姓名"""
        locator = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText')
        return self.get_element(locator).text

    @TestLogger.log()
    def delete_member_by_name(self, member='大佬1'):
        """删除群成员"""
        self.click_del_member()
        self.select_contact_by_name(name=member)
        time.sleep(2)
        self.click_sure()
        time.sleep(2)
        self.click_sure_icon()
        time.sleep(2)

    @TestLogger.log()
    def delete_all_member(self):
        """删除所有群成员"""
        time.sleep(2)
        number = self.get_group_members_number()
        while number > 1:
            self.click_del_member()
            self.click_menber_list_first_member()
            time.sleep(2)
            self.click_sure()
            time.sleep(2)
            self.click_sure_icon()
            time.sleep(4)
            self.wait_for_page_load()
            number = number - 1


    @TestLogger.log()
    def get_my_name_in_this_group(self):
        """获取我的群昵称"""
        time.sleep(2)
        locator = (MobileBy.XPATH, '//*[@name="我的群昵称"]/following-sibling::XCUIElementTypeStaticText[1]')
        els = self.get_element(locator)
        return els.text

    @TestLogger.log()
    def get_group_name(self):
        """获取群名称"""
        time.sleep(2)
        locator = (MobileBy.XPATH, '//*[@name="群名称"]/following-sibling::XCUIElementTypeStaticText[1]')
        els = self.get_element(locator)
        return els.text


    @TestLogger.log()
    def add_member_by_name(self, member='大佬1'):
        """添加群成员"""
        from pages import SelectHeContactsDetailPage
        from pages import ChatWindowPage
        if self.is_text_present(member):
            pass
        else:
            self.click_add_member()
            select_he = SelectHeContactsDetailPage()
            select_he.select_one_he_contact_by_name(member)
            select_he.click_sure_icon()
            chat = ChatWindowPage()
            chat.wait_for_page_load()
            time.sleep(3)
            chat.click_setting()

    @TestLogger.log()
    def add_member_by_phone(self, phone):
        """添加群成员"""
        from pages import SelectHeContactsDetailPage
        if self.is_text_present(phone):
            pass
        else:
            self.click_add_member()
            select_he = SelectHeContactsDetailPage()
            select_he.click_name_attribute_by_name(phone, 20)
            select_he.click_sure_icon()



    # @TestLogger.log()
    # def make_sure_gruop_member_number_is_certain_number(self, number=3, names=[]):
    #     """确保群人数多少人（默认群人数是3人）"""
    #     from pages import ChatWindowPage
    #     member = self.get_group_members_number()
    #     # 少于需求,则添加
    #     if member < number:
    #         need = number - member
    #         self.click_add_member()
    #         from pages import SelectContactsPage
    #         select = SelectContactsPage()
    #         for name in names:
    #             select.select_one_contact_by_name(name)
    #         select.click_sure_bottom()
    #         chat = ChatWindowPage()
    #         chat.wait_for_page_load()
    #         time.sleep(3)
    #         chat.click_setting()
    #         need -= 1
    #
    #     elif member > number:
    #         need = member - number
    #         while need > 0:
    #             self.click_del_member()
    #             self.click_menber_list_first_member()
    #             time.sleep(2)
    #             self.click_sure()
    #             time.sleep(2)
    #             self.click_sure_icon()
    #             time.sleep(2)
    #             need -= 1
    #
    #     else:
    #         time.sleep(3)
    #

    @TestLogger.log("获取控件数量")
    def get_element_count(self):
        els=self.get_elements(self.__locators["再次邀请"])
        return len(els)

    @TestLogger.log()
    def _find_menu(self, locator):
        if not self._is_element_present(locator):
            # 找不到就翻页找到菜单再点击，
            self.swipe_by_direction(self.__locators['菜单区域'], 'up')
            if self._is_element_present(locator):
                return
            self.swipe_by_direction(self.__locators['菜单区域'], 'down')
            if self._is_element_present(locator):
                return
            raise AssertionError('页面找不到元素：{}'.format(locator))

    @TestLogger.log()
    def get_group_total_member(self):
        """获取群成员总人数"""
        self._find_menu(self.__class__.__locators['群成员(2人)'])
        el = self.get_element(self.__class__.__locators['群成员(2人)'])
        res = re.search(r"\d+", el.text)
        if res:
            return int(res.group())
        else:
            return 0

    @TestLogger.log()
    def click_group_member_show(self):
        """点击群成员展示>"""
        self._find_menu(self.__class__.__locators['群成员展开>'])
        self.click_element(self.__class__.__locators["群成员展开>"])

    @TestLogger.log()
    def click_back(self):
        """点击返回"""
        self.click_element(self.__class__.__locators["返回"])

    @TestLogger.log()
    def click_modify_group_name(self):
        """点击 修改群聊名称"""
        self._find_menu(self.__locators['修改群聊名称'])
        self.click_element(self.__locators['修改群聊名称'])

    @TestLogger.log()
    def click_QRCode(self):
        """点击群二维码"""
        self.click_element(self.__locators['群二维码'])

    @TestLogger.log()
    def click_my_card(self):
        """点击我在本群的昵称"""
        self._find_menu(self.__locators['我在本群的昵称'])
        self.click_element(self.__locators['我在本群的昵称'])

    @TestLogger.log()
    def click_group_manage(self):
        """点击群管理"""
        self._find_menu(self.__locators['群管理'])
        self.click_element(self.__locators['群管理'])

    # @TestLogger.log()
    # def get_switch_undisturb_status(self):
    #     """获取消息免打扰开关状态"""
    #     self._find_menu(self.__locators['消息免打扰开关'])
    #     el = self.get_element(self.__locators['消息免打扰开关'])
    #     return el.get_attribute("checked") == "true"

    # @TestLogger.log()
    # def get_chat_set_to_top_switch_status(self):
    #     """获取置顶聊天开关状态"""
    #     self._find_menu(self.__locators['置顶聊天开关'])
    #     el = self.get_element(self.__locators['置顶聊天开关'])
    #     return el.get_attribute("checked") == "true"
    #
    # @TestLogger.log()
    # def click_chat_set_to_top_switch(self):
    #     """点击置顶聊天开关"""
    #     self._find_menu(self.__locators['置顶聊天开关'])
    #     self.click_element(self.__locators['置顶聊天开关'])

    @TestLogger.log()
    def click_find_chat_record(self):
        """点击查找聊天内容"""
        self.click_element(self.__class__.__locators['查找聊天内容'])

    @TestLogger.log()
    def click_clear_chat_record(self):
        """点击清空聊天记录"""
        self._find_menu(self.__locators['清空聊天记录'])
        self.click_element(self.__locators['清空聊天记录'])

    @TestLogger.log()
    def wait_clear_chat_record_confirmation_box_load(self, timeout=10, auto_accept_alerts=True):
        """等待 聊天记录清除确认框"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self.is_text_present("是否清空聊天记录")
            )
        except:
            message = "页面在{}s内，没有加载成功".format(timeout)
            raise AssertionError(
                message
            )
        return self

    @TestLogger.log()
    def wait_exist_and_delete_confirmation_box_load(self, timeout=10, auto_accept_alerts=True):
        """等待 解散群成员确认框加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self.is_text_present("解散群")
            )
        except:
            message = "页面在{}s内，没有加载成功".format(timeout)
            raise AssertionError(
                message
            )
        return self

    @TestLogger.log()
    def click_confirm(self):
        """点击确认"""
        self.click_element(self.__locators['确认'])

    @TestLogger.log()
    def click_cancel(self):
        """点击取消"""
        self.click_element(self.__locators['取消'])

    @TestLogger.log()
    def click_sure_exit_group(self):
        """点击确定退出"""
        self.click_element(self.__locators['退出'])
        time.sleep(3)

    @TestLogger.log()
    def click_sure(self):
        """点击确定"""
        self.click_element(self.__locators['确定'])

    @TestLogger.log()
    def scroll_to_bottom(self):
        """滑到菜单底部"""
        self.wait_until(
            condition=lambda d: self.get_element(self.__locators['群聊设置'])
        )
        self.swipe_by_direction(self.__locators['菜单区域'], 'up')

    @TestLogger.log()
    def click_determine(self):
        """点击确定"""
        self.click_element(self.__locators['确定'])

    @TestLogger.log()
    def click_search_chat_record(self):
        """点击 查找聊天内容"""
        self.click_element(self.__class__.__locators['查找聊天内容'])

    @TestLogger.log()
    def is_enabled_of_group_name_save_button(self):
        """判断群名称保存按钮是否置灰"""
        return self._is_enabled(self.__class__.__locators['完成'])

    @TestLogger.log()
    def get_edit_query_text(self):
        """获取输入框文本"""
        el = self.get_element((MobileBy.ID, 'com.chinasofti.rcs:id/edit_query'))
        text = el.get_attribute("text")
        return text

    @TestLogger.log()
    def wait_for_qecode_load(self, timeout=15, auto_accept_alerts=True):
        """等待群二维码加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self.is_text_present("该二维码7天内")
            )
        except:
            message = "页面在{}s内，没有加载成功".format(str(timeout))
            raise AssertionError(
                message
            )
        return self

    @TestLogger.log()
    def click_qecode_share_button(self):
        """点击群二维码分享按钮"""
        times=10
        while times>0:
            time.sleep(1)
            if self.get_elements(self.__class__.__locators['二维码转发']):
                self.click_element(self.__class__.__locators['二维码转发'])
                break
            else:
                times -= 1
                if self.get_elements(self.__class__.__locators['二维码重置']):
                   self.click_element(self.__class__.__locators['二维码重置'])
                   time.sleep(1)

        return False

    @TestLogger.log()
    def click_qecode_download_button(self):
        """点击群二维码下载按钮"""
        times = 10
        while times > 0:
            time.sleep(1)
            if self.get_elements(self.__class__.__locators['二维码下载']):
                self.click_element(self.__class__.__locators['二维码下载'])
                break
            else:
                times -= 1
                if self.get_elements(self.__class__.__locators['二维码重置']):
                    self.click_element(self.__class__.__locators['二维码重置'])
                    time.sleep(1)

        return False

    @TestLogger.log()
    def click_qecode_back_button(self):
        """点击群二维码页面返回按钮"""
        self.click_element(self.__class__.__locators['二维码返回'])

    @TestLogger.log()
    def wait_for_group_manage_load(self, timeout=8, auto_accept_alerts=True):
        """等待群管理页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self.is_text_present("群管理")
            )
        except:
            message = "页面在{}s内，没有加载成功".format(str(timeout))
            raise AssertionError(
                message
            )
        return self

    @TestLogger.log()
    def click_group_manage_back_button(self):
        """点击群管理页面返回按钮"""
        self.click_element(self.__class__.__locators['群管理返回'])

    @TestLogger.log()
    def click_group_manage_transfer_button(self):
        """点击群主管理权转让按钮"""
        self.click_element(self.__class__.__locators['群主管理权转让'])

    @TestLogger.log()
    def click_group_manage_disband_button(self):
        """点击解散群按钮"""
        self.click_element(self.__class__.__locators['解散群'])

    @TestLogger.log()
    def click_sure_disband_button(self):
        """点击确定解散"""
        self.click_element(self.__class__.__locators['解散'])

    @TestLogger.log("点击添加成员")
    def click_add_number(self):
        els = self.get_elements(self.__locators["com.chinasofti.rcs:id/iv_avatar"])
        el = els[1]
        el.click()

    @TestLogger.log()
    def wait_for_share_group_load(self, timeout=15, auto_accept_alerts=True):
        """等待群管理页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self.is_text_present("分享群口令邀请好友进群")
            )
        except:
            message = "页面在{}s内，没有加载成功".format(str(timeout))
            raise AssertionError(
                message
            )
        return self

    @TestLogger.log()
    def delete_group_chat_and_exit(self):
        """删除群聊"""
        times = 3
        while times > 0:
            try:
                self.click_element(self.__locators['删除并退出'])
                break
            except:
                times -= 1
                pass
        self.click_element(self.__locators['退出'])
        self.wait_until(timeout=30, auto_accept_permission_alert=False, condition=lambda d: self.is_text_present("说点什么"))

    @TestLogger.log()
    def is_exists_back_button(self):
        """是否存在返回按钮"""
        return self._is_element_present2(self.__class__.__locators["返回"])

    @TestLogger.log()
    def get_group_members_image_number(self):
        """获取群成员头像数"""
        locator = (MobileBy.XPATH,
                   '//*[contains(@name,"cc_chat_groupchat_add_normal")]/../../../preceding-sibling::XCUIElementTypeCell[*]')
        if self._is_element_present2(locator):
            els = self.get_elements(locator)
            return len(els)

    @TestLogger.log()
    def get_group_number_text(self):
        """获取群成员文本"""
        if self._is_element_present2(self.__class__.__locators["群成员文本"]):
            el = self.get_element(self.__class__.__locators["群成员文本"])
            return el.text

    @TestLogger.log()
    def is_exists_element_by_text(self, text):
        """是否存在指定元素"""
        return self._is_element_present2(self.__class__.__locators[text])

    @TestLogger.log()
    def click_element_by_text(self, text):
        """点击指定元素"""
        self.click_element(self.__class__.__locators[text])

    @TestLogger.log()
    def get_element_value_by_text(self, text):
        """获取指定元素的文本"""
        if self._is_element_present2(self.__class__.__locators[text]):
            el = self.get_element(self.__class__.__locators[text])
            return el.text

    @TestLogger.log()
    def click_group_members_image_by_name(self, name):
        """点击指定群成员头像"""
        locator = (MobileBy.XPATH, '//*[contains(@name,"%s")]/preceding-sibling::XCUIElementTypeImage[1]' % name)
        self.click_element(locator)

    @TestLogger.log('判断页面存在元素')
    def is_element_present_by_locator(self, locator='转发'):
        if self._is_element_present(self.__locators[locator]):
            return True
        else:
            return False

    @TestLogger.log()
    def input_search_group_members(self, name):
        """输入搜索群成员"""
        self.input_text(self.__class__.__locators['群成员搜索框'], name)
