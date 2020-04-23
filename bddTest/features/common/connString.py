import os
# To-adjust: bv-app file path
# if add app inside the app folder, can use this path: 
# '.\\features\\app\\bvDev.apk'
app_path = os.path.abspath('D:\\bddTest\\bvDev.apk')

# To-adjust: the connection string info
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['app'] = app_path
desired_caps['appPackage'] = 'sg.com.trustedsource.boardVision'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

serverPortal = 'http://127.0.0.1:4723/wd/hub'