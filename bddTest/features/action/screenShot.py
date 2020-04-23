from functools import wraps
import time

def screenshot_for_when_action(func):
    @wraps(func)
    def wrapper(context, *args, **kwargs):
        try:
            func(context, *args, **kwargs)
        except:
            c_time=time.strftime('%Y%m%d-%H%M')
            errorname = c_time + func.__name__
            # To-adjust: screenshot file path
            picname = "D:\\bddTest\\screen_shots\\"+errorname+".png"
            context.driver.get_screenshot_as_file(picname)
            raise Exception(func.__name__+" is not stable.")
    return wrapper

def screenshot_for_then_action(func):
    @wraps(func)
    def wrapper(context, *args, **kwargs):
        try:
            func(context, *args, **kwargs)
        except:
            c_time = time.strftime('%Y%m%d-%H%M')
            errorname = c_time + func.__name__
            # To-adjust: screenshot file path
            picname = "D:\\bddTest\\screen_shots\\"+errorname + ".png"
            context.driver.get_screenshot_as_file(picname)
            raise Exception(func.__name__+" can't normally work.")
    return wrapper
