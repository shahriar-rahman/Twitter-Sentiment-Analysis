#import datetime
#currentDT = datetime.datetime.now()
#Today=datetime.datetime.today().weekday();
#print(Today);
#print ("Current Year is: %d" % currentDT.year)
#Year= str(currentDT.year)[2:4];
#print(Year);
#print ("Current Month is: %d" % currentDT.month)
#print ("Current Day is: %d" % currentDT.day)
#print ("Current Hour is: %d" % currentDT.hour)
#print ("Current Minute is: %d" % currentDT.minute)
#print ("Current Second is: %d" % currentDT.second)
#print ("Current Microsecond is: %d" % currentDT.microsecond)
import webbrowser;
#webbrowser.get('firefox').open_new_tab("https://www.google.com/");
from time import *;
import sys
import csv;
import time
from playsound import playsound
import os;
from pynput.keyboard import Key, Controller;
keyboard = Controller();
from pynput.mouse import Button, Controller;
from textblob  import TextBlob;
mouse = Controller();
#print(time.strftime("%H:%M"))
#os.system('explorer E:\\january\\apps\\');(0.8);
#os.startfile (r"E:\january\apps\jalarm.lnk");
#mouse.position=(564, 1059);
#mouse.press(Button.left);mouse.release(Button.left);sleep(0.5);
#keyboard.type("cd PycharmProjects");sleep(0.1);keyboard.press(Key.enter);keyboard.release(Key.enter);sleep(0.1);
#keyboard.type("cd SentimentAnalysis");sleep(0.1);keyboard.press(Key.enter);keyboard.release(Key.enter);sleep(0.1);
#keyboard.type("JanuaryAlarm.py");sleep(0.1);keyboard.press(Key.enter);keyboard.release(Key.enter);sleep(0.1);
#mouse.press(Button.left);mouse.release(Button.left);(0.5);
#keyboard.press(Key.alt);keyboard.press(Key.tab); keyboard.release(Key.alt);sleep(0.1);
#keyboard.release(Key.tab);sleep(0.1);
import tkinter;

    #if "search for" in formatText:
        #wordSplit = formatText.split("search for ");
       #encryptedSearch = str(wordSplit).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        #keyboard.type(encryptedSearch);


#elif "wait" in formatText or "hang on" in formatText:
from tkinter import *

import time
import math
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk  # Python 2

DELAY = 100
CIRCULAR_PATH_INCR = 10

sin = lambda degs: math.sin(math.radians(degs))
cos = lambda degs: math.cos(math.radians(degs))

class Celestial(object):
    # Constants
    COS_0, COS_180 = cos(0), cos(180)
    SIN_90, SIN_270 = sin(90), sin(270)

    def __init__(self, x, y, radius):
        self.x, self.y = x, y
        self.radius = radius

    def bounds(self):
        """ Return coords of rectangle surrounding circlular object. """
        return (self.x + self.radius*self.COS_0,   self.y + self.radius*self.SIN_270,
                self.x + self.radius*self.COS_180, self.y + self.radius*self.SIN_90)

def circular_path(x, y, radius, delta_ang, start_ang=0):
    """ Endlessly generate coords of a circular path every delta angle degrees. """
    ang = start_ang % 360
    while True:
        yield x + radius*cos(ang), y + radius*sin(ang)
        ang = (ang+delta_ang) % 360

def update_position(canvas, id, celestial_obj, path_iter):
    celestial_obj.x, celestial_obj.y = next(path_iter)  # iterate path and set new position
    # update the position of the corresponding canvas obj
    x0, y0, x1, y1 = canvas.coords(id)  # coordinates of canvas oval object
    oldx, oldy = (x0+x1) // 2, (y0+y1) // 2  # current center point
    dx, dy = celestial_obj.x - oldx, celestial_obj.y - oldy  # amount of movement
    canvas.move(id, dx, dy)  # move canvas oval object that much
    # repeat after delay
    canvas.after(DELAY, update_position, canvas, id, celestial_obj, path_iter)

top = tk.Tk()
top.title('Circular Path')
top.overrideredirect(1);
top.geometry('%dx%d+%d+%d' % (500, 600, 10, 535));top.attributes("-alpha", .10)

canvas = tk.Canvas(top, bg='black', height=500, width=500)
canvas.pack()

sol_obj = Celestial(250, 250, 25)
planet_obj1 = Celestial(250+100, 250, 15)
sol = canvas.create_oval(sol_obj.bounds(), fill='yellow', width=0)
planet1 = canvas.create_oval(planet_obj1.bounds(), fill='blue', width=0)

orbital_radius = math.hypot(sol_obj.x - planet_obj1.x, sol_obj.y - planet_obj1.y)
path_iter = circular_path(sol_obj.x, sol_obj.y, orbital_radius, CIRCULAR_PATH_INCR)
next(path_iter)  # prime generator

top.after(DELAY, update_position, canvas, planet1, planet_obj1, path_iter)
top.mainloop()






