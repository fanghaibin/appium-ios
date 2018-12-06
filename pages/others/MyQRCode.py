from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger


class MyQRCodePage(BasePage):
    """我的二维码"""
    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.QRCodeActivity'

    __locators = {
        'com.chinasofti.rcs:id/action_bar_root': (MobileBy.ID, 'com.chinasofti.rcs:id/action_bar_root'),
        'android:id/content': (MobileBy.ID, 'android:id/content'),
        'com.chinasofti.rcs:id/id_toolbar': (MobileBy.ID, 'com.chinasofti.rcs:id/id_toolbar'),
        '返回': (MobileBy.ID, 'com.chinasofti.rcs:id/left_back'),
        '我的二维码': (MobileBy.ID, 'com.chinasofti.rcs:id/text_title'),
        'com.chinasofti.rcs:id/contentFrame': (MobileBy.ID, 'com.chinasofti.rcs:id/contentFrame'),
        'com.chinasofti.rcs:id/qr_code_info_view': (MobileBy.ID, 'com.chinasofti.rcs:id/qr_code_info_view'),
        'com.chinasofti.rcs:id/rl_qr_info': (MobileBy.ID, 'com.chinasofti.rcs:id/rl_qr_info'),
        'com.chinasofti.rcs:id/profile_info': (MobileBy.ID, 'com.chinasofti.rcs:id/profile_info'),
        '你大爷': (MobileBy.ID, 'com.chinasofti.rcs:id/twodimension_name_text'),
        'com.chinasofti.rcs:id/twodimensioncode_myprofile_icon': (
            MobileBy.ID, 'com.chinasofti.rcs:id/twodimensioncode_myprofile_icon'),
        'com.chinasofti.rcs:id/my_twodimensionCode': (MobileBy.ID, 'com.chinasofti.rcs:id/my_twodimensionCode'),
        '扫描二维码，添加和飞信': (MobileBy.ID, 'com.chinasofti.rcs:id/textView2'),
        'com.chinasofti.rcs:id/qecode_share_btn': (MobileBy.ID, 'com.chinasofti.rcs:id/qecode_share_btn'),
        'com.chinasofti.rcs:id/qecode_save_btn': (MobileBy.ID, 'com.chinasofti.rcs:id/qecode_save_btn'),
        'android:id/statusBarBackground': (MobileBy.ID, 'android:id/statusBarBackground')
    }

    @TestLogger.log('返回')
    def click_back(self):
        self.click_element(self.__locators['返回'])