import time
from pynput import mouse, keyboard

class InputRecorder():
    def __init__(self, actions):
        self.actions = actions
        self.recording = False
        self.playing = False
        self.mouse_listener = None
        self.keyboard_listener = None
        self.mouse_controller = None

    def stop(self):
        pass

    def play(self):
        def handle_move(action):
            #self.mouse_controller.position(action[1])
            print("move")

        def handle_click(action):
            print("click")
        
        def handle_normal_press(action):
            print("normal press")

        def handle_especial_press(action):
            print("especial press")
        
        d = {"move":handle_move,
             "click":handle_click,
             "press_char":handle_normal_press,
             "press_especial_char":handle_especial_press}
        
        def manage_handlers(action):
            #self.mouse_controller = mouse.Controller()
            d[action[0]](action)

        self.actions.execute(manage_handlers)
       
    def on_move(self, x, y):
        self.actions.add(("move", (x,y)))

    def on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        self.actions.add(("click", (x,y)))

    def on_press(self, key):
        try:
            # print('alphanumeric key {0} pressed'.format(
            #     key.char))
            self.actions.add(("press_char", key.char))
        
        except AttributeError:
            # print('special key {0} pressed'.format(
            #     key))
            if (key != keyboard.Key.ctrl_l and key != keyboard.Key.ctrl_r):
                self.actions.add(("press_especial_char", key))
            
    def start_recording(self):
        #mouse
        self.actions.restart()

        self.mouse_listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click)
        self.mouse_listener.start()

        #keyboard
        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_press)
        self.keyboard_listener.start()


    def show_coordinates(self):
        pass

    def stop_recording(self):
        #self.actions.show()
        #mouse
        self.mouse_listener.stop()

        #keyboard
        self.keyboard_listener.stop()


    def start_recording_clicks(self):
        pass

class InputActions():
    def __init__(self):
        self.actions = []
    
    def add(self, action):
        self.actions.append(action)
    
    def show(self):
        for action in self.actions:
            print(action)

    def restart(self):
        self.actions = []

    def execute(self, f):
        for action in self.actions:
            f(action)

class InputRecorderManager():
    def __init__(self, actions):
        self.actions = actions
    
    def nothing(self):
        pass

