
from utils import clicker
from utils.key_listener import KeyListener



def on_press_a():
    print("a has been pressed")
    clicker.mouse_clicks(clicks=10, interval=0.1)

def on_press_e():
    print("e has been pressed")
    clicker.mouse_clicks(clicks=100, interval=0.1)

if __name__=='__main__':
    kl=KeyListener()
    print("WARNING: Every time you press the 'a' key, the script will click 10 times!")
    kl.add_on_press('a',on_press_a)
    # kl.add_on_press('e',on_press_e)
    kl.start_listening()





