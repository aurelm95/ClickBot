from pynput import keyboard

"""
The main idea code has been extracted form:

    https://stackoverflow.com/questions/11918999/key-listeners-in-python

"""


class KeyListener():
    def __init__(self):
        print("KeyListener initialized. Press 'esc' to stop me.")
        self.key_function_dict={}
    
    def add_on_press(self, key, callback_function):
        self.key_function_dict[key]=callback_function

    def on_press(self,key):
        if key == keyboard.Key.esc:
            return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        
        # if k in ['1', '2', 'left', 'right']:  # keys of interest
        #     print('Key pressed: ' + k)

        try:
            callback_function=self.key_function_dict[k]
            callback_function()
        except KeyError:
            pass

    def start_listening(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()  # start to listen on a separate thread
        listener.join()  # remove if main thread is polling self.keys

if __name__=='__main__':
    kl=KeyListener()

    def p():
        print("Hi")

    kl.add_on_press(key='q',callback_function=p)

    kl.start_listening()



