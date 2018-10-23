from unicodedata import normalize

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from library import config


class BasePage(object):
    """PageObject 应该从该基类继承"""
    ACTIVITY = ''

    @property
    def activity(self):
        return self.__class__.ACTIVITY

    @property
    def driver(self):
        assert isinstance(config.DriverCache.current_driver, webdriver.Remote)
        return config.DriverCache.current_driver

    def _get_platform(self):
        try:
            platform_name = self.driver.desired_capabilities['platformName']
        except Exception as e:
            raise e
        return platform_name.lower()

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def _get_text(self, locator):
        elements = self.get_elements(locator)
        if len(elements) > 0:
            return elements[0].text
        return None

    def _is_text_present(self, text):
        text_norm = normalize('NFD', text)
        source_norm = normalize('NFD', self.get_source())
        return text_norm in source_norm

    def _is_element_present(self, locator):
        elements = self.get_elements(locator)
        return len(elements) > 0

    def _is_visible(self, locator):
        elements = self.get_elements(locator)
        if len(elements) > 0:
            return elements[0].is_displayed()
        return None

    def _is_enabled(self, locator):
        element = self.get_element(locator)
        return element.is_enabled()

    def get_source(self):
        return self.driver.page_source

    def click_element(self, locator):
        self.get_element(locator).click()

    def click_text(self, text, exact_match=False):
        if self._get_platform() == 'ios':
            if exact_match:
                _xpath = u'//*[@value="{}" or @label="{}"]'.format(text, text)
            else:
                _xpath = u'//*[contains(@label,"{}") or contains(@value, "{}")]'.format(text, text)
            self.get_element((MobileBy.XPATH, _xpath)).click()
        elif self._get_platform() == 'android':
            if exact_match:
                _xpath = u'//*[@{}="{}"]'.format('text', text)
            else:
                _xpath = u'//*[contains(@{},"{}")]'.format('text', text)
            self.get_element((MobileBy.XPATH, _xpath)).click()

    def input_text(self, locator, text):
        self.get_element(locator).send_keys(text)

    def swipe_by_direction(self, locator, direction, duration=None):
        element = self.get_element(locator)
        rect = element.rect
        left, right = int(rect['x']) + 1, int(rect['x'] + rect['width']) - 1
        top, bottom = int(rect['y']) + 1, int(rect['y'] + rect['height']) - 1
        width = int(rect['width']) - 2
        height = int(rect['height']) - 2

        if self._get_platform() == 'android':
            if direction.lower() == 'left':
                x_start = right
                x_end = left
                y_start = (top + bottom) // 2
                y_end = (top + bottom) // 2
                self.driver.swipe(x_start, y_start, x_end, y_end, duration)
            elif direction.lower() == 'right':
                x_start = left
                x_end = right
                y_start = (top + bottom) // 2
                y_end = (top + bottom) // 2
                self.driver.swipe(x_start, y_start, x_end, y_end, duration)
            elif direction.lower() == 'up':
                x_start = (left + right) // 2
                x_end = (left + right) // 2
                y_start = bottom
                y_end = top
                self.driver.swipe(x_start, y_start, x_end, y_end, duration)
            elif direction.lower() == 'down':
                x_start = (left + right) // 2
                x_end = (left + right) // 2
                y_start = top
                y_end = bottom
                self.driver.swipe(x_start, y_start, x_end, y_end, duration)

        else:
            if direction.lower() == 'left':
                x_start = right
                x_offset = width
                y_start = (top + bottom) // 2
                y_offset = 0
                self.driver.swipe(x_start, y_start, x_offset, y_offset, duration)
            elif direction.lower() == 'right':
                x_start = left
                x_offset = width
                y_start = -(top + bottom) // 2
                y_offset = 0
                self.driver.swipe(x_start, y_start, x_offset, y_offset, duration)
            elif direction.lower() == 'up':
                x_start = (left + right) // 2
                x_offset = 0
                y_start = bottom
                y_offset = -height
                self.driver.swipe(x_start, y_start, x_offset, y_offset, duration)
            elif direction.lower() == 'down':
                x_start = (left + right) // 2
                x_offset = 0
                y_start = top
                y_offset = height
                self.driver.swipe(x_start, y_start, x_offset, y_offset, duration)

    def swipe_by_percent_on_screen(self, start_x, start_y, end_x, end_y, duration):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        x_start = float(start_x) / 100 * width
        x_end = float(end_x) / 100 * width
        y_start = float(start_y) / 100 * height
        y_end = float(end_y) / 100 * height
        x_offset = x_end - x_start
        y_offset = y_end - y_start
        if self._get_platform() == 'android':
            self.driver.swipe(x_start, y_start, x_end, y_end, duration)
        else:
            self.driver.swipe(x_start, y_start, x_offset, y_offset, duration)

    def page_should_contain_text(self, text):
        if not self._is_text_present(text):
            raise AssertionError("Page should have contained text '%s' "
                                 "but did not" % text)
        return True

    def page_should_not_contain_text(self, text):
        if self._is_text_present(text):
            raise AssertionError("Page should not have contained text '%s'" % text)
            return True

    def page_should_contain_element(self, locator):
        if not self._is_element_present(locator):
            raise AssertionError("Page should have contained element '%s' "
                                 "but did not" % locator)
        return True

    def page_should_not_contain_element(self, locator):
        if self._is_element_present(locator):
            raise AssertionError("Page should not have contained element '%s'" % locator)
        return True

    def element_should_be_disabled(self, locator):
        if self._is_enabled(locator):
            raise AssertionError("Element '%s' should be disabled "
                                 "but did not" % locator)
        return True

    def element_should_be_enabled(self, locator):
        if not self._is_enabled(locator):
            raise AssertionError("Element '%s' should be enabled "
                                 "but did not" % locator)
        return True

    def element_should_be_visible(self, locator):
        if not self.get_element(locator).is_displayed():
            raise AssertionError("Element '%s' should be visible "
                                 "but did not" % locator)
        return True

    def element_should_contain_text(self, locator, expected, message=''):
        actual = self._get_text(locator)
        if expected not in actual:
            if not message:
                message = "Element '%s' should have contained text '%s' but " \
                          "its text was '%s'." % (locator, expected, actual)
            raise AssertionError(message)
        return True

    def element_should_not_contain_text(self, locator, expected, message=''):
        actual = self._get_text(locator)
        if expected in actual:
            if not message:
                message = "Element '%s' should not contain text '%s' but " \
                          "it did." % (locator, expected)
            raise AssertionError(message)
        return True

    def element_text_should_be(self, locator, expected, message=''):
        element = self.get_element(locator)
        actual = element.text
        if expected != actual:
            if not message:
                message = "The text of element '%s' should have been '%s' but " \
                          "in fact it was '%s'." % (locator, expected, actual)
            raise AssertionError(message)
        return True

    def wait_until(self, condition, timeout=8, auto_accept_permission_alert=True):
        def execute_condition(driver):
            """如果有弹窗，自动允许"""

            def get_accept_permission_handler(d):
                """获取允许权限弹窗的方法句柄"""
                try:
                    alert = d.switch_to.alert
                    return alert.accept
                except:
                    alert = self.get_elements((MobileBy.XPATH, '//*[@text="始终允许"]')) \
                            or self.get_elements((MobileBy.XPATH, '//*[@text="允许"]'))
                    if not alert:
                        return False
                    return alert[0].click

            if auto_accept_permission_alert:
                if self.driver.current_activity in [
                    'com.android.packageinstaller.permission.ui.GrantPermissionsActivity',
                    '.permission.ui.GrantPermissionsActivity'
                ]:
                    need = True
                    while need:
                        try:
                            WebDriverWait(self.driver, 1).until(
                                get_accept_permission_handler
                            )()
                        except:
                            need = False
            return condition(driver)

        wait = WebDriverWait(self.driver, timeout)
        return wait.until(execute_condition)

    def wait_for_page_load(self, timeout=8, auto_accept_alerts=True):
        """默认使用activity作为判断页面是否加载的条件，继承类应该重写该方法"""
        self.wait_until(
            lambda d: self.driver.current_activity == self.__class__.ACTIVITY,
            timeout,
            auto_accept_alerts
        )
        return self
