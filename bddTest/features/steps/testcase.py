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
from features.common.userData import singleCompanyAcc2,PW2
from features.common.exception import *
from features.action.userPageActions import *
from features.action.screenShot import *
from features.action.testSupDocToolbar import *

from behave import given, when, then  # pylint: disable=no-name-in-module

@when('successful login and in home page')
@screenshot_for_when_action
def Successful_login(context):
    pass

@then('check date displayed')
@screenshot_for_then_action
def Check_date_displayed(context):
    wait_load_by_id(context.driver, 3, HomePage.dateId_id)
    today = time.strftime("%d %b %Y")
    index_today = today.split(" ")
    #if date is correct
    dayElement = get_text_by_id(context.driver, HomePage.dateId_id)
    assert index_today[
        0] == dayElement, "Date display wrongly. Date displayed is " + dayElement
    #if month and year correct
    m_y_Element = get_text_by_id(context.driver, HomePage.monthId_id)
    mAndY = m_y_Element.split(" ")
    judge1 = index_today[1] == mAndY[0]
    judge2 = index_today[2] == mAndY[1]
    assert judge1 == True, "Month display wrongly. Month displayed is " + mAndY[0]
    assert judge2 == True, "Year display wrongly. Year displayed is " + mAndY[1]

@then('check search bar function with searching "{string1}"')
@screenshot_for_then_action
def Check_searchbar(context, string1):
    click_by_id(context.driver, HomePage.searchBarBtn_id)
    search_bar = check_displayed_by_id(context.driver, HomePage.searchTextBox_id)
    assert search_bar == True, "Search bar isn't selected properly."
    check_event = WithUnhandledEvent(context.driver)
    if check_event == True:
        # To-adjust: the search content string
        sendkeys_by_id(context.driver, HomePage.searchTextBox_id, string1)
        click_by_id(context.driver, HomePage.searchBtn_id)
        wait_load_by_id(context.driver, 10, HomePage.searchTextBox_id)
        blank_list = WithUnhandledEvent(context.driver)
        assert blank_list == False, "Search function doesn't work properly."
        clear_text_by_id(context.driver, HomePage.searchTextBox_id)
        # To-adjust: the search content string
        sendkeys_by_id(context.driver, HomePage.searchTextBox_id, "test")
        click_by_id(context.driver, HomePage.searchBtn_id)
        wait_load_by_xpath(context.driver, 10, HomePage.topEventText2_xp)
        event_text = get_text_by_xpath(context.driver, HomePage.topEventText2_xp)
        assert "test" in event_text.lower(), "Search function doesn't work properly."
        click_by_id(context.driver, HomePage.searchCloseBtn_id)
    else:
        pass
    wait_load_by_id(context.driver, 3, HomePage.homePageLayout_id)

@given('display home page')
def Display_home_page(context):
    pass

@when('click third button')
@screenshot_for_when_action
def Click_third_button(context):
    click_by_id(context.driver, BotBar.userPage_id)
    wait_load_by_id(context.driver, 3, UserPage.userPic_id)

@then('display user page')
@screenshot_for_then_action
def Display_user_page(context):
    user = check_displayed_by_id(context.driver, UserPage.userPic_id)
    assert user == True, "Failed to navigate to user page."

@when('click second button')
@screenshot_for_when_action
def Click_second_button(context):
    click_by_id(context.driver, BotBar.itemPage_id)
    wait_load_by_id(context.driver, 3, ItemPage.itemPageTitle_id)

@then('display item page')
@screenshot_for_then_action
def Display_item_page(context):
    item = check_displayed_by_id(context.driver, ItemPage.itemPageTitle_id)
    assert item == True, "Failed to navigate to item page."


@then(
    'check search bar function by serching "{string1}" and search "{string2}", then test filter'
    )
@screenshot_for_then_action
def Check_searchbar_filter(context, string1, string2):
    click_by_id(context.driver, ItemPage.searchBarBtn_id)
    search_bar = check_displayed_by_id(context.driver,
                                    ItemPage.searchTextBox_id)
    assert search_bar == True, "Search bar isn't selected properly."
    # To-adjust: the search content string
    sendkeys_by_id(context.driver, ItemPage.searchTextBox_id, string1)
    click_by_id(context.driver, ItemPage.searchBtn_id)
    wait_load_by_id(context.driver, 5, ItemPage.searchTextBox_id)
    blank_list = WithUnhandledEvent(context.driver)
    assert blank_list == False, "Search function doesn't work properly."
    clear_text_by_id(context.driver, ItemPage.searchTextBox_id)
    # To-adjust: the search content string
    sendkeys_by_id(context.driver, ItemPage.searchTextBox_id, string2)
    click_by_id(context.driver, ItemPage.searchBtn_id)
    wait_load_by_xpath(context.driver, 7, ItemPage.topItemText_xp)
    event_text = get_text_by_xpath(context.driver, ItemPage.topItemText_xp)
    assert "test" in event_text.lower(), "Search function doesn't work properly."
    click_by_id(context.driver, ItemPage.searchCloseBtn_id)
    wait_load_by_id(context.driver, 5, ItemPage.filterBtn_id)
    # Test filter for resolution
    click_by_id(context.driver, ItemPage.filterBtn_id)
    wait_load_by_id(context.driver, 2, ItemPage.meetingSwitch_id)
    click_by_id(context.driver, ItemPage.meetingSwitch_id)
    click_by_id(context.driver, ItemPage.scheduleSwitch_id)
    click_by_id(context.driver, ItemPage.showResultsBtn_id)
    wait_load_by_id(context.driver, 10, ItemPage.itemPageTitle_id)
    test_filter_resolution(context.driver)
    # Test filter for schedule
    click_by_id(context.driver, ItemPage.filterBtn_id)
    wait_load_by_id(context.driver, 2, ItemPage.resolutionSwitch_id)
    click_by_id(context.driver, ItemPage.resolutionSwitch_id)
    click_by_id(context.driver, ItemPage.scheduleSwitch_id)
    click_by_id(context.driver, ItemPage.showResultsBtn_id)
    wait_load_by_id(context.driver, 10, ItemPage.itemPageTitle_id)
    test_filter_schedule(context.driver)
    # Test filter for meeting
    click_by_id(context.driver, ItemPage.filterBtn_id)
    wait_load_by_id(context.driver, 2, ItemPage.scheduleSwitch_id)
    click_by_id(context.driver, ItemPage.scheduleSwitch_id)
    click_by_id(context.driver, ItemPage.meetingSwitch_id)
    click_by_id(context.driver, ItemPage.showResultsBtn_id)
    wait_load_by_id(context.driver, 10, ItemPage.itemPageTitle_id)
    test_filter_meeting(context.driver)

@when('click first button')
@screenshot_for_when_action
def Click_first_button(context):
    click_by_id(context.driver, BotBar.homePage_id)

@then('display home page again')
@screenshot_for_then_action
def Display_home_page_2(context):
    home = check_displayed_by_id(context.driver, HomePage.dateId_id)
    assert home == True, "Failed to navigate to home page."

@given('check any unhandled resolution exists')
def Check_resolution(context):
    # select one type of events to run test, with filter
    # first select resolution for test
    wait_load_by_id(context.driver, 3, HomePage.filterBtn_id)
    clickFilter(context.driver)
    # select resolution to test
    wait_load_by_id(context.driver, 2, HomePage.filterpopup_id)
    switchMeeting(context.driver)
    switchSchedule(context.driver)
    clickShowResults(context.driver)
    wait_load_by_id(context.driver, 3, HomePage.filterBtn_id)
    reso_todo = WithUnhandledEvent(context.driver)
    if reso_todo == True:
        print('Unhandled resolution exists and needs to test.')
    else:
        print('No unhandled resolution.')

@when('unhandled resolution exists')
@screenshot_for_when_action
def empty_act(context):
    pass

@then('test basic function in resolution')
@screenshot_for_then_action
def handle_resolution_procedure(context):
    reso_todo = WithUnhandledEvent(context.driver)
    if reso_todo == True:
        # determine one or many to-dos
        time.sleep(2)
        if IsSingle(context.driver) == True:
            resolution_name = get_text_by_id(context.driver,
                                            HomePage.singleEventText_id)
            click_by_id(context.driver, HomePage.singleEventMark_id)

        else:
            resolution_name = get_text_by_xpath(context.driver,
                                                HomePage.topEventText_xp)
            click_by_xpath(context.driver, HomePage.topEvent)

        wait_load_by_id(context.driver, 10, HomePage.resolutionMark_id)
        # Test pdf tool
        test_approval_doc_toolbar(context.driver)

        if check_displayed_by_id(context.driver, HomePage.supDocBtn_id):
            click_by_id(context.driver, HomePage.supDocBtn_id)
            time.sleep(4)
            if check_displayed_by_id(context.driver, HomePage.actionMenu_id):
                test_sup_doc_toolbar(context.driver)
                press_back_button(context.driver)
            else:
                click_by_xpath(context.driver, HomePage.topMultiSupDoc_xpath)
                test_sup_doc_toolbar(context.driver)
                press_back_button(context.driver)
                press_back_button(context.driver)
        # Test "Add remarks" function
        # which can be optimised by checking the result in email
        click_by_id(context.driver, HomePage.actionMenu_id)
        click_by_id(context.driver, HomePage.addRemarksBtn_id)
        wait_load_by_id(context.driver, 3, HomePage.remarksBox_id)
        sendkeys_by_id(context.driver, HomePage.remarksBox_id,
                    "Add some remarks here.")

        click_by_id(context.driver, HomePage.updateRemarksBtn_id)
        wait_load_by_id(context.driver, 5, HomePage.actionMenu_id)
        click_by_id(context.driver, HomePage.actionMenu_id)
        testRemarks = get_text_by_id(context.driver, HomePage.editRemarksBtn_id)
        assert testRemarks == "Edit Remarks", addRemarksException
        # To-adjust: so far it can only approve one resolution
        click_by_id(context.driver, HomePage.approveBtn_id)
        wait_load_by_id(context.driver, 2, HomePage.continueWithRemarks_id)
        click_by_id(context.driver, HomePage.continueWithRemarks_id)
        # To-do: I want to add a picture comparison here.
        # To distinguish whether signature is loaded or not
        time.sleep(6)
        popup = check_displayed_by_id(context.driver, HomePage.accessFilePop_id)
        if popup:
            wait_load_by_id(context.driver, 3, HomePage.allowAccessBtn_id)
            click_by_id(context.driver, HomePage.allowAccessBtn_id)
        wait_load_by_id(context.driver, 5, HomePage.loadSignatureBtn_id)
        click_by_id(context.driver, HomePage.loadSignatureBtn_id)
        wait_load_by_id(context.driver, 8, HomePage.continueToAction_id)
        loaded = check_displayed_by_id(context.driver, HomePage.clearSignatureBtn_id)
        assert loaded == True, loadSignatureException
        click_by_id(context.driver, HomePage.continueToAction_id)
        time.sleep(6)
        optmark = check_displayed_by_id(context.driver, HomePage.otpMark_id)
        if optmark:
            # To-do: OTP part
            # Now can only manually key in
            # After put in the OTP, it directs to another page
            wait_load_by_id(context.driver, 45, HomePage.resoBackBtn_id)
            click_by_id(context.driver, HomePage.resoBackBtn_id)
            wait_load_by_id(context.driver, 8, BotBar.itemPage_id)
        else:
            wait_load_by_id(context.driver, 8, BotBar.itemPage_id)
        # switch to item page, check if the approval is handled
        click_by_id(context.driver, BotBar.itemPage_id)
        top_item_name = get_text_by_xpath(context.driver, ItemPage.topItem_xp)
        assert resolution_name==top_item_name, handleApprovalException
        click_by_id(context.driver, BotBar.homePage_id)

        # testing case following
    else:
        clickFilter(context.driver)
        wait_load_by_id(context.driver, 2, HomePage.filterpopup_id)
        switchSchedule(context.driver)
        switchMeeting(context.driver)
        clickShowResults(context.driver)

@given('check any unhandled schedule exists')
def check_unhandled_schedule(context):
    # after testing in resolution page, it should direct to home page for coming test.
    # test schedules
    wait_load_by_id(context.driver, 5, HomePage.filterBtn_id)
    clickFilter(context.driver)
    wait_load_by_id(context.driver, 2, HomePage.filterpopup_id)
    switchResolution(context.driver)
    switchMeeting(context.driver)
    clickShowResults(context.driver)
    context.sche_todo = WithUnhandledEvent(context.driver)
    if context.sche_todo == True:
        print('Unhandled schedule exist.\n')
    else:
        print('No unhandled schedule.\n')

@when('unhandled shcedule exists')
@screenshot_for_when_action
def empty_act_1(context):
    pass

@then('test basic function in shcedule')
@screenshot_for_then_action
def test_schedule(context):
    if context.sche_todo == True:
        if IsSingle(context.driver) == True:
            schedule_name = get_text_by_id(context.driver, HomePage.singleEventText_id)
            click_by_id(context.driver, HomePage.singleEventMark_id)
        else:
            schedule_name = get_text_by_xpath(context.driver,
                                            HomePage.topEventText_xp)
            click_by_xpath(context.driver, HomePage.topEvent_xp)

        time.sleep(1)
        schedulePage = check_displayed_by_id(context.driver, HomePage.schedulePageTitle_id)
        assert schedulePage, "Failed to direct to view schedule page."
        click_by_id(context.driver, HomePage.scheVote_id)
        click_by_id(context.driver, HomePage.scheBackBtn_id)
        time.sleep(2)
        checkExitPop = check_displayed_by_id(context.driver, HomePage.scheExitPopup_id)
        assert checkExitPop, "Back to home page confirmation popup didn't appear as expected."
        click_by_id(context.driver, HomePage.scheNoExitBtn_id)
        click_by_id(context.driver, HomePage.scheUpdateBtn_id)
        try:
            wait_load_by_id(context.driver, 10, HomePage.homePageLayout_id)
        except:
            raise Exception("Failed to direct to home page after submitting vote.")
        click_by_id(context.driver, BotBar.itemPage_id)
        top_event_name = get_text_by_xpath(context.driver, ItemPage.topItem_xp)
        assert top_event_name==schedule_name, handleScheduleException
        click_by_id(context.driver, BotBar.homePage_id)

    else:
        clickFilter(context.driver)
        wait_load_by_id(context.driver, 3, HomePage.filterpopup_id)
        switchMeeting(context.driver)
        switchResolution(context.driver)
        clickShowResults(context.driver)

@given('check any unhandled meeting exists')
def check_meeting(context):
    wait_load_by_id(context.driver, 3, HomePage.filterBtn_id)
    clickFilter(context.driver)
    wait_load_by_id(context.driver, 2, HomePage.filterpopup_id)
    switchResolution(context.driver)
    switchSchedule(context.driver)
    clickShowResults(context.driver)
    time.sleep(2)
    meet_todo = WithUnhandledEvent(context.driver)
    if meet_todo == True:
        print('Unhandled meeting exists.')
    else:
        print('No unhandled meeting.')

@when('unhandled meeting exists')
@screenshot_for_when_action
def empty_act_2(context):
    pass

@then('test basic function in meeting')
@screenshot_for_then_action
def test_meeting(context):
    meet_todo = WithUnhandledEvent(context.driver)
    if meet_todo:
        if IsSingle(context.driver):
            meeting_name = get_text_by_id(context.driver,
                                        HomePage.singleEventText_id)
            click_by_id(context.driver, HomePage.singleEventMark_id)
        else:
            meeting_name = get_text_by_xpath(context.driver,
                                            HomePage.topEventText_xp)
            click_by_xpath(context.driver, HomePage.topEvent_xp)
        wait_load_by_id(context.driver, 5, HomePage.otherDocBtn_id)
        click_by_id(context.driver, HomePage.otherDocBtn_id)
        otherDoc = check_displayed_by_id(context.driver,
                                        HomePage.otherDocMark_id)
        assert otherDoc == True, "Couldn't switch to other Documents page."
        # Check if additional document exists.
        # To-do: Need to distinguish different types of agenda and whether recused or not
        if check_displayed_by_id(context.driver, HomePage.noMeetingDataMark_id):
            pass
        else:
            if check_displayed_by_id(context.driver, HomePage.singleDocMark_id):
                click_by_id(context.driver, HomePage.singleDocMark_id)
                wait_load_by_id(context.driver, 7, HomePage.pdfPage_id)
                test_meeting_other_doc_toolbar(context.driver)
                press_back_button(context.driver)
            else:
                click_by_xpath(context.driver, HomePage.topMultiDoc_xpath)
                wait_load_by_id(context.driver, 7, HomePage.pdfPage_id)
                test_meeting_other_doc_toolbar(context.driver)
                press_back_button(context.driver)

        wait_load_by_id(context.driver, 2, HomePage.participantBtn_id)
        click_by_id(context.driver, HomePage.participantBtn_id)
        participant = check_displayed_by_id(context.driver,
                                            HomePage.participantMark_id)
        assert participant == True, "Couldn't switch to participants page."

        wait_load_by_id(context.driver, 3, HomePage.agendaBtn_id)
        ### To-do: this testing scenario can be enriched
        click_by_id(context.driver, HomePage.agendaBtn_id)
        agenda = check_displayed_by_id(context.driver, HomePage.agendaMark_id)
        assert agenda == True, "Couldn't switch to agenda page."
        if check_displayed_by_id(context.driver, HomePage.noMeetingDataMark_id):
            press_back_button(context.driver)
        else: # To-do: Need to distinguish different types of agenda and whether recused or not
            if check_displayed_by_id(context.driver, HomePage.singleAgendaMark_id):
                click_by_id(context.driver, HomePage.singleAgendaMark_id)
                wait_load_by_id(context.driver, 3, HomePage.pdfPage_id)
                test_meeting_agenda_toolbar(context.driver, context.width, context.height)
            else:
                click_by_xpath(context.driver, HomePage.topMultiAgenda_xpath)
                wait_load_by_id(context.driver, 3, HomePage.pdfPage_id)
                test_meeting_agenda_toolbar(context.driver, context.width, context.height)
            click_by_id(context.driver, HomePage.meetingBackBtn_id)
            wait_load_by_id(context.driver, 2, HomePage.filterBtn_id)
