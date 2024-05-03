
#import


from pyparsing import C
import picture #import picture.py

import math
import winsound
import ctypes
from colorama import *
import os
import time
from threading import Timer


#variuble
#num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#setting

#color fix windows
init()

#coppyright

print(Fore.LIGHTCYAN_EX +'''
Welcome to calculator !

Create by aliakbartnt !

It's simple calculator !

''')

#fake proccese


time.sleep(1)
print(Fore.YELLOW +"App launching processing . . .")
print(picture.calculator_ascii)
time.sleep(3)
print(Fore.RED +"App runing")
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
    check = 0 #reset value
    a = None #reset value
    b = None #reset value
    c = None #reset value    
    awnser_1 = str((Fore.LIGHTGREEN_EX +"\n" "Awnser : ")) #It is used to beautify the code

    
    
    #1anti-bug
    try:
            #input
            a = float(input(color_reset+F"Enter num 1 "+dot+color_reset ))
             #input mathematical operations
            c = input(Fore.RESET +"What mathematical operations should be performed? (sqrt,+,-,/,*,**,//) "+dot+color_reset)
            if c in ["sqrt"]:#if user type sqrt dont get b value and do it operation
                a = float(a)
                awnser = math.sqrt(a)
                print(f'{awnser_1}{awnser}')
                check = 1

            else: #if not match sqrt get b input form user
                b = None
                b = float(input(F"Enter num 2 "+dot+color_reset ))
                b = str(b) #change type
                a = str(a) #change type
           #change type
            a = str(a)
            
          
            

     #1anti-bug
            
    except:
        winsound.MessageBeep(winsound.MB_ICONHAND)#sound
        print(Fore.RED +"Please enter number"+color_reset) #consol message
        #message-box
        ctypes.windll.user32.MessageBoxW(0, "Please enter number", "Not Correct", 0 | 0x30)
    #    cal()
    
    
    #2anti-bug
    try:
        #check for c value true
        if c in ['+', '-', '*', '**', '/', '//']:
            
            awnser = eval(a + c + b) #eval mathematical operations 
            print(f'{awnser_1}{awnser}')
            
            
             

        elif c in ["sqrt", None]: #its for dont bug else system
            c = '' #just for else work  

           
            #anti-bug
        else :
            print(Fore.RED +"Undefined mathematical operations")#consol message
              
        z = 'T'       
        
    #2anti-bug        
    except: 
        print(Fore.RED +"Please enter number!"+color_reset)#consol message invalid number
        winsound.MessageBeep(winsound.MB_ICONHAND)#sound
        z = ""
        #message-box
        ctypes.windll.user32.MessageBoxW(0, "Please enter number!", "Not Correct", 0 | 0x30)
        cal()#again run main code
    if z == 'T' :
                check = 1
                z = ''

    if check == 1 : #check awnser code run       
    #if main code end ask user relaunch
        again()
        check = 0 #reset value   



#relaunch code


def again():
    rep = None  #reset value 
    rep = str(input(Fore.LIGHTRED_EX +"\n""Relaunch calculater ? y or n "+dot+color_reset))#user awnser input
    print(Fore.RESET +"") #for color reset with awnser user
    if rep == "y" :   #check user awnser
        cal()#relaunch main code
        
        
    elif rep == "n" :   #check user awnser
        print("5 s to close")    
        def end():#start fake end time
#fake-end-time           
            print("Close now")
            time.sleep(1)
            exit()
            
        t = Timer(5.0, end)#after 5 s end app
        t.start() #start timer  
        
#anti-bug     
    else :
        print(Fore.LIGHTRED_EX +"incorrect value"+color_reset)
        again()
m = 1         
#call main code . at the first lunch app this code work   
if m == 1:
    cal()
    m = 0#reset value    
   
    
