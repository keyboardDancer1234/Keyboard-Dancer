# -*- coding: utf-8 -*-
# Program Name: Keyboard Dancer
# Author: Charles Blake
# Contact: blabspublic@gmail.com
# Propose: To make tapping my fingers on the desk when I’m bored far more entertaining.
# Usage: Play on the home keys! :D
# License: GNU GPLv3. The full license text can be found at gnu.org

import sys

print "-------------------------------------------------"
print "|              Keyboard Dancer                  |"
print "|                 GNU GPLV3                     |"
print "|Please hack and share for the sake of freedom! |"
print "-------------------------------------------------"

from Tkinter import * #We're using the Tkinter library extensively

root = Tk()
root.title("Keyboard Dancer")
w = Canvas(root,width=400,height=50)  #Define the main window
w.pack()

#############
# Variables #
#############
states = [False,False,False,False,False,False,False,False]

#############
# Functions #
#############
def processGraphics():
	w.delete(ALL)
	if states[0]:
		w.create_rectangle(0,0,50,50,fill="blue")
	if states[1]:
		w.create_rectangle(50,0,100,50,fill="red")
	if states[2]:
		w.create_rectangle(100,0,150,50,fill="green")
	if states[3]:
		w.create_rectangle(150,0,200,50,fill="black")
	if states[4]:
		w.create_rectangle(200,0,250,50,fill="black")
	if states[5]:
		w.create_rectangle(250,0,300,50,fill="green")
	if states[6]:
		w.create_rectangle(300,0,350,50,fill="red")
	if states[7]:
		w.create_rectangle(350,0,400,50,fill="blue")

################
# Key bindings #
################
def key(event):
	if event.char == 'a' and states[0] == False:
		states[0]=True;

	if event.char == 's' and states[1] == False:
		states[1]=True;

	if event.char == 'd' and states[2] == False:
		states[2]=True;

	if event.char == 'f' and states[3] == False:
		states[3]=True;

	if event.char == 'j' and states[4] == False:
		states[4]=True;

	if event.char == 'k' and states[5] == False:
		states[5]=True;

	if event.char == 'l' and states[6] == False:
		states[6]=True;

	if event.char == ';' and states[7] == False:
		states[7]=True;

	print states
	processGraphics()


def release(event):
	if event.char == 'a' and states[0] == True:
		states[0]=False;

	if event.char == 's' and states[1] == True:
		states[1]=False;

	if event.char == 'd' and states[2] == True:
		states[2]=False;

	if event.char == 'f' and states[3] == True:
		states[3]=False;

	if event.char == 'j' and states[4] == True:
		states[4]=False;

	if event.char == 'k' and states[5] == True:
		states[5]=False;

	if event.char == 'l' and states[6] == True:
		states[6]=False;

	if event.char == ';' and states[7] == True:
		states[7]=False;

	print states
	processGraphics()

def callback(event):
	print "clicked at", event.x, event.y

#######################
# Logic and listeners #
#######################
w.bind("<Key>", key)
w.bind("<KeyRelease>",release)
w.bind("<Button-1>", callback)
w.focus_set()
root.mainloop()
