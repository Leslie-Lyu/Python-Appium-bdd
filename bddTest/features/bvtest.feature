# -- FILE: bddTest/feature/bvTest.feature
Feature: Conduct test scenarios on BV

    Scenario: Launch app and direct to login page
        Given opened BV app
        When switch to login page
        Then should see login page
        
    # For this scenario, can user Scenario Outline for optimize
    # Use a table to pass login info and realize multi account login
    Scenario: Test login function
        Given login page is displayed
        When key in user account and wrong password "11111111"
        Then wrong passrord message prompts
        When key in correct password
        Then it directs to PIN page
        And create/Keyin PIN

    Scenario: If login succeeded
        Then should see home page

    Scenario: Test homepage date display
        When successful login and in home page
        Then check date displayed
        # To-do:
        And check search bar function with searching "xxxxxxxx"

    Scenario: Test navbar
        Given display home page
        When click third button
        Then display user page
        When click second button
        Then display item page
        And check search bar function by serching "xxxxxxxx" and search "test", then test filter
        When click first button
        Then display home page again

    Scenario: Test unhandled resolution
        Given check any unhandled resolution exists
        When unhandled resolution exists
        Then test basic function in resolution

    Scenario: Test unhandled shcedule
        Given check any unhandled schedule exists
        When unhandled shcedule exists
        Then test basic function in shcedule
    
    Scenario: Test unhandled meeting
        Given check any unhandled meeting exists
        When unhandled meeting exists
        Then test basic function in meeting

    Scenario: Test user page
        Given directs to user page
        When switch to my profile page
        Then check login info
        When directs to setting page
        Then change PIN and check if saved successfully
        And signout in the end



