import os
import time

from appium import webdriver
from features.steps import login
from features.action.actions import *
from features.action.unhandled_event import *
from features.page.BotBar import BotBar
from features.page.HomePage import HomePage
from features.page.ItemPage import ItemPage
from features.page.UserPage import UserPage
from features.common.userData import singleCompanyAcc2, PW2
from features.common.exception import *
from features.action.userPageActions import *
from features.action.screenShot import *
from features.action.testSupDocToolbar import *

from behave import given, when, then  # pylint: disable=no-name-in-module


@given('directs to user page')
@screenshot_for_when_action
def direct_to_userpage(context):
    try:
        click_by_id(context.driver, BotBar.userPage_id)
        wait_load_by_id(context.driver, 3, UserPage.myProfilePage_id)
    except:
        raise Exception("Can't switch to user page")


@when('switch to my profile page')
@screenshot_for_when_action
def switch_to_my_profile(context):
    click_by_id(context.driver, UserPage.myProfilePage_id)
    time.sleep(1.5)
    titleText = get_text_by_id(context.driver, UserPage.myProfilePageTitle_id)
    assert titleText == "My Profile", "Fails to direct to My Profile page."


@then('check login info')
@screenshot_for_then_action
def check_login_info(context):
    emailAdd = get_text_by_id(context.driver, UserPage.emailAddress_id)
    assert emailAdd == singleCompanyAcc2, "User email address not match with login info."


@when('directs to setting page')
@screenshot_for_when_action
def direct_to_setting_page(context):
    click_by_id(context.driver, UserPage.myProfileBackBtn_id)
    wait_load_by_id(context.driver, 2, UserPage.settingPage_id)
    click_by_id(context.driver, UserPage.settingPage_id)
    wait_load_by_id(context.driver, 2, UserPage.changePIN_id)


@then('change PIN and check if saved successfully')
@screenshot_for_then_action
def change_PIN(context):
    click_by_id(context.driver, UserPage.changePIN_id)
    wait_load_by_id(context.driver, 2, UserPage.num0Btn_id)
    KeyIn0000(context.driver)
    wait_load_by_id(context.driver, 2, UserPage.num1Btn_id)
    KeyIn1111(context.driver)
    click_by_id(context.driver, UserPage.confirmPINChange_id)
    wait_load_by_id(context.driver, 2, UserPage.num1Btn_id)
    KeyIn1111(context.driver)
    titleText2 = get_text_by_xpath(context.driver, UserPage.settingTitle_xp)
    assert titleText2 == "Settings", "Error occurs after change PIN."
    press_home_button(context.driver)
    time.sleep(0.5)
    press_multitask_button(context.driver)
    context.driver.tap([(context.width * 0.5, context.height * 0.5)], 200)
    wait_load_by_id(context.driver, 3, UserPage.num1Btn_id)
    KeyIn0000(context.driver)
    check_PIN = check_displayed_by_id(context.driver, UserPage.errorMark_id)
    if check_PIN:
        print("PIN changed successfully.")
    else:
        raise Exception("PIN change function is down.")
    click_by_id(context.driver, UserPage.erasePIN_id)
    KeyIn1111(context.driver)
    try:
        wait_load_by_id(context.driver, 2, UserPage.changePIN_id)
    except:
        raise Exception("Previous PIN is gone but new is not saved.")


@then('signout in the end')
@screenshot_for_then_action
def signout(context):
    click_by_id(context.driver, UserPage.settingPageBackBtn_id)
    click_by_id(context.driver, UserPage.signOutBtn_id)
    signoutPopCheck = check_displayed_by_id(context.driver,
                                            UserPage.signOutPop_id)
    assert signoutPopCheck == True, "Sign out button not work."
    click_by_id(context.driver, UserPage.signOutDecline_id)
    declineCheck = check_displayed_by_id(context.driver,
                                        UserPage.signOutBtn_id)
    assert declineCheck == True, "Sign out decline button not work."
    click_by_id(context.driver, UserPage.signOutBtn_id)
    wait_load_by_xpath(context.driver, 2, UserPage.signOut_xp)
    click_by_xpath(context.driver, UserPage.signOut_xp)
    try:
        wait_load_by_id(context.driver, 2, UserPage.loginPage_id)
        signoutCheck = check_displayed_by_id(context.driver,
                                            UserPage.loginPage_id)
    except:
        raise Exception("Fails to sign out.")
