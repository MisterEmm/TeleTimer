#!/usr/bin/env python
import os
import sys
import math
import time
import unicornhat as unicorn
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Receiver Switch
GPIO.setup(14, GPIO.OUT) # Relay
GPIO.setup(26, GPIO.OUT) # LED

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.8)
width,height=unicorn.get_shape()

def restart():
        
    GPIO.output(14,True)
    GPIO.output(26,True)
    unicorn.set_all(0,255,0)
    unicorn.show()
    time.sleep(0.3)
    GPIO.output(14,False)
    GPIO.output(26,False)
    unicorn.off()
    time.sleep(0.2)
    GPIO.output(14,True)
    GPIO.output(26,True)
    unicorn.set_all(0,255,0)
    unicorn.show()
    time.sleep(0.3)
    GPIO.output(14,False)
    GPIO.output(26,False)
    unicorn.off()
    time.sleep(1)
    print("argv was",sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")
    os.execv(sys.executable, ['python'] + sys.argv)

def bleep():
    z=1
    while z<24:
        if (GPIO.input(12) ==0):
            
            print("Phone Button Pressed")
            time.sleep(1)
            restart()
            
        elif (GPIO.input(16) ==0):
            
            print("Handset Lifted")
            time.sleep(1)
            restart()
        else:
            
            GPIO.output(14,True)
            GPIO.output(26,True)
            unicorn.set_all(255,0,0)
            unicorn.show()
            time.sleep(0.2)
            GPIO.output(14,False)
            GPIO.output(26,False)
            unicorn.off()
            time.sleep(1)
            z += 1
            print(z)
    restart()

def timer1h():
    t=0
    while t<25:
        for y in range(height):
            for x in range(width):
                if (GPIO.input(12) ==0):
            
                    print("Phone Button Pressed")
                    time.sleep(0.2)
                    restart()
                                
                elif (GPIO.input(16) ==0):
            
                    print("Handset Lifted")
                    time.sleep(0.2)
                    restart()
                else:
                    
                    unicorn.set_pixel(x,y,255,0,0)
                    unicorn.show()
                    time.sleep(150)
                    t += 1
                    print(t)
                
def rainbow1min():
    i = 0.0
    offset = 30
    while i<1212:
            i = i + 0.3
            if (GPIO.input(12) ==0):
            
                print("Phone Button Pressed")
                time.sleep(0.2)
                restart()
                                
            elif (GPIO.input(16) ==0):
            
                print("Handset Lifted")
                time.sleep(0.2)
                restart()
            else:
                for y in range(height):
                    for x in range(width):
                            r = 0
                            g = 0
                            r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
                            g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
                            b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
                            r = max(0, min(255, r + offset))
                            g = max(0, min(255, g + offset))
                            b = max(0, min(255, b + offset))
                            unicorn.set_pixel(x,y,int(r),int(g),int(b))
            unicorn.show()
            time.sleep(0.01)
            print(i) #get the count for rainbow duration

#time.sleep(1)
        
timer1h()
rainbow1min()
bleep()