import time
from features.page.HomePage import HomePage
from features.action.actions import click_by_id, click_by_accessibility_id, check_selected_by_id\
                                ,check_displayed_by_xpath, press_back_button, check_displayed_by_id, wait_load_by_id

def test_approval_doc_toolbar(driver):
    click_by_accessibility_id(driver, HomePage.outline_acid)
    assert check_selected_by_id(driver, HomePage.annotation_id), "Open annotation page fails."
    press_back_button(driver)
    wait_load_by_id(driver, 2, HomePage.resolutionMark_id)

    click_by_accessibility_id(driver, HomePage.search_acid)
    check_searchbox = check_displayed_by_id(driver, HomePage.searchBox_id)
    assert check_searchbox, "PDF search button doesn't work properly."
    # To-do: test search function
    click_by_id(driver, HomePage.searchBack_id)

    click_by_accessibility_id(driver, HomePage.settings_acid)
    time.sleep(0.5)
    check_setting = check_displayed_by_xpath(driver, HomePage.settingPopup_xp)
    assert check_setting, "Setting popup window doesn't appear as expected."
    press_back_button(driver)

    click_by_accessibility_id(driver, HomePage.share_acid)
    wait_load_by_id(driver, 3, HomePage.sharePopupTitle_id)
    check_share1 = check_displayed_by_id(driver, HomePage.shareMenu_id)
    check_share2 = check_displayed_by_id(driver, HomePage.shareOption_id)
    assert check_share1 and check_share2, "Share window doesn't appear as expected."
    press_back_button(driver)

    click_by_accessibility_id(driver, HomePage.grid_acid)
    check_grid = check_displayed_by_id(driver, HomePage.gridSideBar_id)
    assert check_grid, "Grid side bar doesn't appear as expected."
    press_back_button(driver)

def test_sup_doc_toolbar(driver):
    click_by_accessibility_id(driver, HomePage.outline_acid)
    check_annotation = check_selected_by_id(driver, HomePage.annotation_id)
    check_docinfo = check_selected_by_id(driver, HomePage.docInfo_id)
    assert check_annotation and not check_docinfo, "In support document page, outline top bar default status is not correct."
    click_by_id(driver, HomePage.docInfo_id)
    check_annotation = check_selected_by_id(driver, HomePage.annotation_id)
    check_docinfo = check_selected_by_id(driver, HomePage.docInfo_id)
    assert not check_annotation and check_docinfo, "In support document page, outline top bar cannot switch correctly."
    press_back_button(driver)
    wait_load_by_id(driver, 2, HomePage.resolutionMark_id)

    click_by_accessibility_id(driver, HomePage.search_acid)
    check_searchbox = check_displayed_by_id(driver, HomePage.searchBox_id)
    assert check_searchbox, "In support document page, PDF search button doesn't work properly."
    # To-do: test search function
    click_by_id(driver, HomePage.searchBack_id)

    click_by_accessibility_id(driver, HomePage.settings_acid)
    time.sleep(0.5)
    check_setting = check_displayed_by_xpath(driver, HomePage.settingPopup_xp)
    assert check_setting, "In support document page, setting popup window doesn't appear as expected."
    press_back_button(driver)

    click_by_accessibility_id(driver, HomePage.grid_acid)
    check_grid = check_displayed_by_id(driver, HomePage.gridSideBar_id)
    assert check_grid, "In support document page, grid side bar doesn't appear as expected."
    press_back_button(driver)

def test_meeting_other_doc_toolbar(driver):
    click_by_accessibility_id(driver, HomePage.search_acid)
    check_searchbox = check_displayed_by_id(driver, HomePage.searchBox_id)
    assert check_searchbox, "In meeting document page, PDF search button doesn't work properly."
    # To-do: test search function
    click_by_id(driver, HomePage.searchBack_id)

    click_by_accessibility_id(driver, HomePage.settings_acid)
    time.sleep(0.5)
    check_setting = check_displayed_by_xpath(driver, HomePage.settingPopup_xp)
    assert check_setting, "In meeting document page, setting popup window doesn't appear as expected."
    press_back_button(driver)

    click_by_accessibility_id(driver, HomePage.share_acid)
    wait_load_by_id(driver, 3, HomePage.sharePopupTitle_id)
    check_share1 = check_displayed_by_id(driver, HomePage.shareMenu_id)
    check_share2 = check_displayed_by_id(driver, HomePage.shareOption_id)
    assert check_share1 and check_share2, "In meeting document page, share window doesn't appear as expected."
    press_back_button(driver)

    click_by_accessibility_id(driver, HomePage.grid_acid)
    check_grid = check_displayed_by_id(driver, HomePage.gridSideBar_id)
    assert check_grid, "In meeting document page, grid side bar doesn't appear as expected."
    press_back_button(driver)

    click_by_accessibility_id(driver, HomePage.outline_acid)
    check_annotation = check_selected_by_id(driver, HomePage.annotation_id)
    assert check_annotation, "In meeting document page, annotation page default status is not correct."
    press_back_button(driver)

def test_meeting_agenda_toolbar(driver, width, height):
    click_by_accessibility_id(driver, HomePage.search_acid)
    check_searchbox = check_displayed_by_id(driver, HomePage.searchBox_id)
    assert check_searchbox, "In meeting document page, PDF search button doesn't work properly."
    # To-do: test search function
    click_by_id(driver, HomePage.searchBack_id)

    click_by_accessibility_id(driver, HomePage.settings_acid)
    time.sleep(0.5)
    check_setting = check_displayed_by_xpath(driver, HomePage.settingPopup_xp)
    assert check_setting, "In meeting document page, setting popup window doesn't appear as expected."
    press_back_button(driver)

    click_by_accessibility_id(driver, HomePage.share_acid)
    wait_load_by_id(driver, 3, HomePage.sharePopupTitle_id)
    check_share1 = check_displayed_by_id(driver, HomePage.shareMenu_id)
    check_share2 = check_displayed_by_id(driver, HomePage.shareOption_id)
    assert check_share1 and check_share2, "In meeting document page, share window doesn't appear as expected."
    press_back_button(driver)

    click_by_accessibility_id(driver, HomePage.grid_acid)
    check_grid = check_displayed_by_id(driver, HomePage.gridSideBar_id)
    assert check_grid, "In meeting document page, grid side bar doesn't appear as expected."
    driver.tap([(width*0.2, height*0.5)], 200)

    click_by_accessibility_id(driver, HomePage.outline_acid)
    check_outline = check_selected_by_id(driver, HomePage.outline_id)
    check_annotation = check_selected_by_id(driver, HomePage.annotation_id)
    assert check_outline and not check_annotation, "Outline top bar default status is not correct."
    click_by_id(driver, HomePage.annotation_id)
    check_outline = check_selected_by_id(driver, HomePage.outline_id)
    check_annotation = check_selected_by_id(driver, HomePage.annotation_id)
    assert not check_outline and check_annotation, "Outline top bar cannot switch correctly."
    press_back_button(driver)
    wait_load_by_id(driver, 2, HomePage.agendaBtn_id)
