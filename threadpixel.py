from sense_hat import SenseHat
from time import sleep
import random
import threading

sense = SenseHat()
white = [255,255,255]
black = [0,0,0]
red = [255,0,0]
green = [0,255,0]
blue = [0,0, 255]
orange = [255,128,0]
pink = [255,0,255]
yellow = [255,255,0]
purple = [128,0,255]
colour = [white, red, green, blue, orange, pink, yellow, purple]

count = 0
boredom = 1200  # at some point...

def x_pixel(y):
    x = 0
    global count
    while(count < boredom):
        count += 1
        if x == 0:
            c = random.randrange(len(colour))   # random colour from table
            s = 0.05 + random.random()/10       # random speed (maybe set limit?)
        sense.set_pixel(x,y,colour[c])
        sleep(s)
        sense.set_pixel(x,y,black)
        x = (x+1) % 8

def y_pixel(x):
    y = 0
    global count
    while(count < boredom):
        count += 1
        if y == 0:
            c = random.randrange(len(colour))   # random colour from table
            s = 0.05 + random.random()/10       # random speed (maybe set limit?)
        sense.set_pixel(x,y,colour[c])
        sleep(s)
        sense.set_pixel(x,y,black)
        y = (y+1) % 8   

sense.clear()
random.seed()
# we're launching five threads which each run one pixel line (this should be a list)
t = []
t.append(threading.Thread(target=x_pixel,args=[2]))
t.append(threading.Thread(target=x_pixel,args=[5]))
t.append(threading.Thread(target=x_pixel,args=[7]))
t.append(threading.Thread(target=y_pixel,args=[3]))
t.append(threading.Thread(target=y_pixel,args=[6]))
t.append(threading.Thread(target=y_pixel,args=[7]))
for thread in t:
    thread.start()






