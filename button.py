#Poll Raspberry Pi Buttons and control LEDS
#By Tyler Spadgenske

import RPi.GPIO as gpio
import time

class Poll():
    def __init__(self):
        self.DEBUG = True
        
        
        #Put pins in variables
        self.left_button = 4
        self.center_button = 27
        self.right_button = 24
               

        #Setup pins and board
        gpio.setmode(gpio.BCM)
        gpio.setup(self.center_button, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(self.right_button, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(self.left_button, gpio.IN, pull_up_down=gpio.PUD_UP)

        
        self.first = ''

        self.center_press = 0
        self.right_press = 0
        self.left_press = 0

    def reset(self):
        self.first = ''

        self.center_press = 0
        self.right_press = 0
        self.left_press = 0
        
    def poll(self): #Returns first button pressed
        #Variables for press count (one for each button)
        self.center_press = 0
        self.right_press = 0
        self.left_press = 0

        #Check for button presses
        while True:
            self.first = self.check()
            if self.first != '':
                break
        time.sleep(.5)
        return self.first

    def check(self):
        center_input = gpio.input(self.center_button)
        left_input = gpio.input(self.left_button)
        right_input = gpio.input(self.right_button)
        if center_input == gpio.LOW:
            if self.center_press > 0:
                if self.DEBUG:
                    print('ADMIN: Console button 2 has been pressed')
                self.first = 1
            
            else:
                if self.DEBUG:
                    pass
            self.center_press += 1

        #Right buttons stuff
        if right_input == gpio.LOW:
            if self.right_press > 0:
                if self.DEBUG:
                    print('ADMIN: Console button 3 has been pressed')
                self.first = 2
            
            else:
                if self.DEBUG:
                    pass
            self.right_press += 1

        #Left button stuff
        if left_input == gpio.LOW:
            if self.left_press > 0:
                if self.DEBUG:
                    print('ADMIN: Console button 1 has been pressed')
                self.first = 0
            
            else:
                if self.DEBUG:
                    pass
            self.left_press += 1

        return self.first

if __name__ == '__main__':
    test = Poll()
    while True:
        test.first = ''
        winner = test.poll()
    print (winner)
