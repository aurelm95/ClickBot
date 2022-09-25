import time

import pyautogui


def get_mouse_position():
    return pyautogui.position()

def mouse_clicks(button='left', clicks=1, interval=0.25):
    pyautogui.click(button=button, clicks=clicks, interval=interval)



if __name__=='__main__':
    pass
