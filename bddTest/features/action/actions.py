from selenium.webdriver.support.ui import WebDriverWait
from features.page.LoginPage import LoginPage
from features.page.ItemPage import ItemPage

def click_by_id(driver, element_id):
    driver.find_element_by_id(element_id).click()

def click_by_xpath(driver, element_xpath):
    driver.find_element_by_xpath(element_xpath).click()

def click_by_accessibility_id(driver, element_accessbility_id):
    driver.find_element_by_accessibility_id(element_accessbility_id).click()

def click_by_android_uiautomator(driver, android_uiautomator):
    driver.find_element_by_android_uiautomator(android_uiautomator).click()

def wait_load_by_id(driver, time, element_id):
    WebDriverWait(driver, time).until(
        lambda sdriver: driver.find_element_by_id(element_id).is_displayed())

def wait_load_by_xpath(driver, time, element_xpath):
    WebDriverWait(driver,
                time).until(lambda sdriver: driver.find_element_by_xpath(
                    element_xpath).is_displayed())

def wait_load_by_accessbility_id(driver, time, element_accessbility_id):
    WebDriverWait(driver, time).until(
        lambda sdriver: driver.find_element_by_accessibility_id(
            element_accessbility_id).is_displayed())

def check_displayed_by_id(driver, element_id):
    try:
        driver.find_element_by_id(element_id).is_displayed()
        return True
    except:
        return False

def check_displayed_by_xpath(driver, element_xpath):
    try:
        driver.find_element_by_xpath(element_xpath).is_displayed()
        return True
    except:
        return False

def check_selected_by_id(driver, element_id):
    return driver.find_element_by_id(element_id).is_selected()

def check_selected_by_xpath(driver, element_xpath):
    return driver.find_element_by_xpath(element_xpath).is_selected()

def sendkeys_by_id(driver, element_id, keys):
    driver.find_element_by_id(element_id).send_keys(keys)

def sendkeys_by_xpath(driver, element_xpath, keys):
    driver.find_element_by_xpath(element_xpath).send_keys(keys)

def get_text_by_id(driver, element_id):
    text = driver.find_element_by_id(element_id).text
    return text

def get_text_by_xpath(driver, element_xpath):
    text = driver.find_element_by_xpath(element_xpath).text
    return text

def clear_text_by_id(driver, element_id):
    driver.find_element_by_id(element_id).click()
    driver.keyevent(123)
    text = driver.find_element_by_id(element_id).text
    for i in range(0, len(text)):
        driver.keyevent(67)

def clear_text_by_xpath(driver, element_xpath):
    driver.find_element_by_xpath(element_xpath).click()
    driver.keyevent(123)
    text = driver.find_element_by_xpath(element_xpath).text
    for i in range(0, len(text)):
        driver.keyevent(67)

def press_back_button(driver):
    driver.keyevent(4)

def press_home_button(driver):
    driver.keyevent(3)
    
def press_multitask_button(driver):
    driver.keyevent(187)

# Key in a "0000" PIN
def keyInPIN(driver):
    wait_load_by_id(driver, 8, LoginPage.eraseBtn_id)
    for i in range(4):
        click_by_id(driver, LoginPage.numb10_id)

def test_func(element_id):
    # context.driver.find_element_by_id(element_id).click()
    pass

def test_filter_resolution(driver):
    elements = driver.find_elements_by_id(ItemPage.itemTypeText_rssid)
    for element in elements:
        assert element.text == "RESOLUTION", "Filter doesn't work as expected."

def test_filter_schedule(driver):
    elements = driver.find_elements_by_id(ItemPage.itemTypeText_rssid)
    for element in elements:
        assert element.text == "SCHEDULE", "Filter doesn't work as expected."

def test_filter_meeting(driver):
    elements = driver.find_elements_by_id(ItemPage.itemTypeText_rssid)
    for element in elements:
        assert element.text == "MEETING", "Filter doesn't work as expected."
