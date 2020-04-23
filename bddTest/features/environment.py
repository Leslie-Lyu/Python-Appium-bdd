import os
from features.common.connString import *
from appium import webdriver


def before_feature(context, feature):
    context.driver = webdriver.Remote(serverPortal, desired_caps)
    context.width = context.driver.get_window_size()['width']
    context.height = context.driver.get_window_size()['height']

def after_feature(context, feature):
    context.driver.quit()