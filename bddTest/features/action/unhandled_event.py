import time
from features.page.HomePage import HomePage
from features.action.actions import click_by_id

def clickFilter(driver):
    click_by_id(driver, HomePage.filterBtn_id)


def clickShowResults(driver):
    click_by_id(driver, HomePage.showResultsBtn_id)


def switchResolution(driver):
    click_by_id(driver, HomePage.resolutionSwitch_id)


def switchMeeting(driver):
    click_by_id(driver, HomePage.meetingSwitch_id)


def switchSchedule(driver):
    click_by_id(driver, HomePage.scheduleSwitch_id)


def IsSingle(driver):
    try:
        driver.find_element_by_id(HomePage.singleEventMark_id).is_displayed()
        return True
    except:
        return False

def WithUnhandledEvent(driver):
    time.sleep(1)
    try:
        driver.find_element_by_id(HomePage.noDataMark_id).is_displayed()
        return False
    except:
        return True