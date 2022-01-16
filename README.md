# Jeopardy Pi Edition
Play Jeopardy on your Raspberry Pi updated to work with Python 3.  Tested with Raspberry Pi 4 model B and Python 3.9.

## Setup
Instructions for setting up the project are as follows.

### Hardware
To setup the Pi you will need:
1.  Raspberry Pi with Python 3 installed
2.  Three momentary push button switches (switches are closed when pressed then opened when pushed)

Wire up the circuit by following the diagram below.  For longer wires you may need to add a resistor in the button circuit to prevent phantom button presses.

Connect one side of each button to the following GPIO pins.  

| GPIO Pin | Physical Header Pin |
| -------- | ------------------- |
| GPIO4 | header pin 7 |
| GPIO27 | header pin 13 | 
| GPIO24 | header pin 18 |


The other sides of the buttons go to ground pins per the diagram.

| Physical Header Pin |
| ------------------- |
| Header pin 9 |
| Header pin 14 |
| Header pin 20 |


![Fritzing Diagram](https://github.com/GitOffMyGrass/Jeopardy/blob/master/Jeopardy_Buzzer_Fritzing.jpg?raw=true)


Please note that on the Raspberry Pi 4, the physical pin number and GPIO pin numbers are different.  Please check the [pinout](https://www.tomshardware.com/reviews/raspberry-pi-gpio-pinout,6122.html) for information. 


You can change the GPIO pin numbers by changing these values in [button.py](https://github.com/GitOffMyGrass/Jeopardy/blob/master/button.py).  Please note these numbers refer to the GPIO pin numbers, not the physical header pin numbers.

```sh
#Put pins in variables
self.left_button = 4
self.center_button = 27
self.right_button = 24
```


### Software Setup

1.  Clone this project

```sh
git clone https://github.com/GitOffMyGrass/jeopardy.git

```

2.  Change to the source directory
```sh
cd jeopardy
```

3.  Launch the application
```sh
python start.py
```

### Questions
You can edit the files in the "games" directory to create your own questions and answers.  The examples are pretty self-explanatory.


# Original project information
Original instruction can be found at:<br />
Follow these instructions:</br>
http://hackaday.io/project/3721/instructions
http://hackaday.io/project/3721-game-show-emulator/log/12365

# Note:
This software is designed to be used with the Raspberry Pi. If you would like to run Jeopardy on a Windows or Ubuntu please use Adam Beagle's <a href='https://github.com/adambeagle/jeoparpy'>jeoparpy software</a>. 

