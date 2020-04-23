import os
import time

from features.page.LoginPage import LoginPage
from features.action.actions import *
from features.common.userData import *
from appium import webdriver
# from hamcrest import *
from hamcrest import assert_that, equal_to_ignoring_case
from features.page.HomePage import HomePage
from features.action.screenShot import *

from behave import given, when, then  # pylint: disable=no-name-in-module

@given('opened BV app')
def Open_BV_app(context):
    pass

@when('switch to login page')
@screenshot_for_when_action
def Switch_to_login_page(context):
    wait_load_by_id(context.driver, 8, LoginPage.welcomeImageId_id)
    click_by_id(context.driver, LoginPage.continueBtn1_id)

    wait_load_by_id(context.driver, 8, LoginPage.welcomeImageId2_id)
    click_by_id(context.driver, LoginPage.continueBtn2_id)

@then('should see login page')
@screenshot_for_then_action
def Detect_login_page(context):
    try:
        wait_load_by_id(context.driver, 8, LoginPage.emailAddBtn_id)
        click_by_id(context.driver, LoginPage.emailAddBtn_id)
    except:
        raise Exception("Can't direct to login page.")

@given('login page is displayed')
def Empty_step(context):
    pass


@when('key in user account and wrong password "{wrong_pw}"')
@screenshot_for_when_action
def Keyin_wrong_pw(context, wrong_pw):
    wait_load_by_xpath(context.driver, 14, LoginPage.userNameBox_xp)
    sendkeys_by_xpath(context.driver, LoginPage.userNameBox_xp, singleCompanyAcc2)
    sendkeys_by_xpath(context.driver, LoginPage.PWBox_xp, wrong_pw)
    click_by_xpath(context.driver, LoginPage.loginBtn_xp)

@then('wrong passrord message prompts')
@screenshot_for_then_action
def Check_wrong_PW(context):
    time.sleep(1)
    wrongMsg = get_text_by_xpath(context.driver, LoginPage.wrongPWMsg_xp)
    stnMSg = "WRONG EMAIL OR PASSWORD."
    # assert wrongMsg == stnMSg, "Password check function does not work properly."

@when('key in correct password')
@screenshot_for_when_action
def Keyin_right_PW(context):
    clear_text_by_xpath(context.driver, LoginPage.PWbox2_xp)
    sendkeys_by_xpath(context.driver, LoginPage.PWbox2_xp, PW2)
    # To-do: can use relative cordinate
    # So this can fit different size mobile device
    context.driver.swipe(908, 1456, 911, 1047)
    click_by_xpath(context.driver, LoginPage.loginBtn_xp)

@then('it directs to PIN page')
@screenshot_for_then_action
def Check_PIN_page(context):
    time.sleep(8)
    context.withoutPIN = check_displayed_by_id(context.driver, LoginPage.createPINId_id)
    assert context.withoutPIN == True, "After login, failed to direct to PIN page."

@then('create/Keyin PIN')
@screenshot_for_then_action
def Pass_PIN_page(context):
    if (context.withoutPIN == False):  # with PIN
        #Forget PIN or not
        forgetPIN = False
        if (forgetPIN == True):
            click_by_id(context.driver, LoginPage.forgetPINBtn_id)
            #To-do: manually key in OTP
            #Create a new PIN
            keyInPIN(context.driver)
            click_by_id(context.driver, LoginPage.confirmBtn_id)
            keyInPIN(context.driver)
        else:
            keyInPIN(context.driver)
    #Create PIN process
    else:
        keyInPIN(context.driver)
        click_by_id(context.driver, LoginPage.confirmBtn_id)
        time.sleep(2)
        keyInPIN(context.driver)

@then('should see home page')
@screenshot_for_then_action
def Check_homepage(context):
    wait_load_by_id(context.driver, 7, HomePage.homePageLayout_id)
    login = check_displayed_by_id(context.driver, HomePage.dateId_id)
    assert login == True, "Failed to login"
