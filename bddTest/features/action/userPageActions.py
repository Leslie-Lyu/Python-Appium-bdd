from features.action.actions import click_by_id
from features.page.UserPage import UserPage

def KeyIn0000(driver):
    for i in range(4):
        click_by_id(driver, UserPage.num0Btn_id)

def KeyIn1111(driver):
    for i in range(4):
        click_by_id(driver, UserPage.num1Btn_id)