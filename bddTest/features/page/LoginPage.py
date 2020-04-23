
class LoginPage():

    # First welcome page
    welcomeImageId_id = "sg.com.trustedsource.boardVision:id/latest_img"
    continueBtn1_id = "sg.com.trustedsource.boardVision:id/continue_to"
    # Second welcome page
    welcomeImageId2_id = "sg.com.trustedsource.boardVision:id/decision"
    continueBtn2_id = "sg.com.trustedsource.boardVision:id/continue_to"
    # Select login page
    emailAddBtn_id = "sg.com.trustedsource.boardVision:id/emailLoginLayout"
    # Key in username and PW page -xpath element
    userNameBox_xp = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText"
    PWBox_xp = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.EditText"
    loginBtn_xp = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button"
    wrongPWMsg_xp = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View"
    PWbox2_xp = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.EditText"
    # Reset password page
    forgetPWBtn_id = "new UiSelector().text(\"Don't remember your password?\")"
    emailAddBox_xp = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText"
    # Id related to PIN
    createPINId_id = "sg.com.trustedsource.boardVision:id/createpin"
    eraseBtn_id = "sg.com.trustedsource.boardVision:id/erase"
    numb10_id = "sg.com.trustedsource.boardVision:id/numb10"
    confirmBtn_id = "sg.com.trustedsource.boardVision:id/resendotp"
    forgetPINBtn_id = "sg.com.trustedsource.boardVision:id/forgot"
