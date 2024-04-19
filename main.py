
#import

import ctypes
from colorama import *
import os
import time
from threading import Timer

#setting

init()

#coppyright

print(Fore.LIGHTCYAN_EX +'''
welcome to calculate !

create by aliakbartnt !

its simple calculate !

''')

#fake proccese


time.sleep(1)
print(Fore.YELLOW +"app launching processing . . .")
time.sleep(3)
print(Fore.RED +"app runing")
time.sleep(1)

#Code cleaning

def cleaner_consol():
    print("\n"*5)
    
cleaner_consol()    

#app source

#Variable

dot = (Fore.LIGHTGREEN_EX +": ")
color_reset = (Fore.RESET +"")

#main source
    
def cal():
    cleaner_consol()
    #Variable
    
    jav = str((Fore.LIGHTGREEN_EX +"\n" "awnser : "))

    
    #input
    
    try:
        
            a = float(input(color_reset+F"enter num 1 "+dot+color_reset ))
            b = float(input(color_reset+"enter num 2 "+dot+color_reset))
            c = str(input(Fore.RESET +"che amal riazi anjam she (+,-,/,*) "))
    except: 
        print(Fore.RED +"please enter number"+color_reset)
        ctypes.windll.user32.MessageBoxW(0, "please enter number", "Not Correct", 1)
        cal()
    
    if c == str("+"):
        proccese = str((a+b))
        
        print(jav + proccese)
    
    elif c == str("-"):
        proccese = str((a-b))
        
        print(jav + proccese)   
    
    elif c == str("/"):
        proccese = str((a/b))
        
        print(jav + proccese) 
    
    elif c == str("*"):
        proccese = str((a*b))
        
        print(jav + proccese)  
    
    else :
        print(Fore.RED +"amaliat namoskhas")
        

    again()   



#relaunch code


def again():
    rep = str(input(Fore.LIGHTRED_EX +"\n""relunch calculate ? y or n "+dot+color_reset))
    print(Fore.RESET +"")
    if rep == "y" :   
        cal()
        
        
    elif rep == "n" :
        print("5 s to close")    
        def end():
            print("colose now")
            time.sleep(1)
        t = Timer(5.0, end)
        t.start()   
    
    else :
        again()
cal()    
    
    
