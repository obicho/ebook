ebook
=====

This is an open source e-reader project designed to work on Raspberry Pi with a Pervasive Display 2.7 inch screen.

The vision is to build an e-reader OS which comes with a kernel and GUI that work nicely for a e-ink display.

![ebook](test.jpg "Output")


### Development environment setup
You can acquire the actual hardware and wire up them up according to the following instructions:

https://github.com/repaper/gratis

http://learn.adafruit.com/repaper-eink-development-board-arm-linux-raspberry-pi-beagle-bone-black/overview

Alternatively, you can also jumpstart developing on linux (emulator mode) and output to an image file for the purpose of software development.

### Tutorial for actual hardware
1. Install PIL in your Python environemnt
2. Github the code from this repo
3. Run 
```
python TextFormatter.py
```

### Tutorial for emulator mode

1. Install PIL in your Python environemnt
2. Github the code from this repo
3. Run 
```
python TextFormatter2.py
```


<h3>Upcoming features</h3>
- Parse uPub format
- Book sharing feature
- Display from the web - simple UI



