
#import

import time
from threading import Timer


from installer import install, check_python_version  #import installer.py
#install()
if __name__ == "__main__": #run this code if this file is main file
    print("wait a minute")
    # run installer
    time.sleep(2)
    install()   
    time.sleep(2)
    check_python_version()
#from installer import check_python_version #import installer.py
#check_python_version()
import picture #import picture.py
import platform
import math
import winsound
import ctypes
from colorama import *
import os


import yaml
time.sleep(2)

#language = 'en'
# select directory
def cfg_messages(config):
    
    config_path = os.path.join(os.path.dirname(__file__), 'config.yml')
    if not os.path.exists(config_path): #check config.yml exist or not
                print("Error: config.yml not found!")
                time.sleep(3) # fake timer
                default_config = { #default config
                    'language': 'en'
                } 
                with open(config_path, 'w', encoding='utf-8') as file: #write default config
                    yaml.dump(default_config, file) 
                config = default_config #set config to default config
    #print (config_path) debug
    else: #if config.yml exist
        
        with open(config_path, 'r', encoding='utf-8') as file: #open config.yml
            config = yaml.safe_load(file) #load config.yml
            if 'language' not in config or config['language'] not in ['en', 'fa']:#check config.yml is empty or not
                print("Error: Invalid config.yml! . default config loaded") #error message
                config = {'language': 'en'} #set default config
                with open(config_path, 'w', encoding='utf-8') as file:
                    yaml.dump(config, file)
        
    #lang input
    try: 
        lang_in = input(Fore.RESET + "Enter language (en/fa): " + Fore.RESET).strip()
        if lang_in not in ['en', 'fa']:  # اگر مقدار نامعتبر وارد شود
            print(Fore.RED + "Invalid language selected! Defaulting to 'en'." + Fore.RESET)
            lang_in = 'en'

        # update config.yml
        if config.get('language') != lang_in:
            config['language'] = lang_in
            with open(config_path, 'w', encoding='utf-8') as file:
                yaml.dump(config, file) #success message

    except ValueError as e:  
        print(Fore.RED + str(e) + Fore.RESET)
        lang_in = config.get('language', 'en')  # if error default language is en
    return config
    #language = config.get('language', 'en') #get language from config.yml
    



def load_messages(lang): #load messages from lang folder
    try:
        
        lang_dir = os.path.join(os.path.dirname(__file__), 'lang', lang) #lang directory
        messages_path = os.path.join(lang_dir, 'messages.yml') #messages.yml path
        

        if not os.path.exists(messages_path): #check messages.yml exist or not
            print(f"Error: {messages_path} not found!") #error message
            exit()
    
        with open(messages_path, 'r', encoding='utf-8') as file: #open messages.yml
            return yaml.safe_load(file) #load messages.yml
    
    except yaml.YAMLError as e: #check error in messages.yml
        print(f"Error in {messages_path}: {e}") #error message
        exit()
config = {}  # Initialize config
config = cfg_messages(config)  # Call cfg_messages function
language = config.get('language', 'en')  # Get language from config        
try:
    messages = load_messages(language) #load messages
except Exception as e: #check error in messages.yml
    print(f"Critical error: {e}") #error message
    exit()
if config['language'] == 'fa':  
    for key, value in messages.items(): # rotate charter per line (loop)
        if isinstance(value, str):  # check its str 
            messages[key] = '\n'.join(line[::-1] for line in value.splitlines()) #rotate charter per line 


 # default language is fa (if not value in config.yml)
#variable
#num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Fore.LIGHTGREEN_EX +"your language is: "+language)
time.sleep(2)
#setting
if platform.system() == "Windows": #nt = windows
    #terminal (cmd) color fix for windows
    init()

#copyright 
# !!! dont touch my copyright my app license is MIT And you must cite the source. !!!
def run():
    print(Fore.LIGHTCYAN_EX +messages['welcome']) 

    #fake process


    time.sleep(3)
    print(Fore.YELLOW +messages['app-launching'])
    print(picture.calculator_ascii)
    time.sleep(3)
    print(Fore.RED +messages['app-running'])
    time.sleep(1)

#Code cleaning

def cleaner_consol():
    print("\n"*5)
    
cleaner_consol()    

#app source

#Variable

run()

dot = (Fore.LIGHTGREEN_EX +": ")
color_reset = (Fore.RESET +"")

#main source
    
def cal():
    
     #call run code      
    cleaner_consol()
    #Variable
    check = 0 #reset value
    a = None #reset value
    b = None #reset value
    c = None #reset value    
    answer_1 = str((Fore.LIGHTGREEN_EX +"\n"+ messages['Answer']+dot)) #It is used to beautify the code

    
    
    #1anti-bug
    try:
            #input
            a = float(input(color_reset+messages['in-num1']+dot+color_reset )) 
             #input mathematical operations
            c = input(Fore.RESET +messages['operation']+dot+color_reset)
            #a = str(a)
            if c in ["sqrt"]:#if user type sqrt dont get b value and do it operation
               # a = int(a)
                if a >= 0:
                    c = str(c)
                    a = float(a)
                    answer = math.sqrt(a)
                    print(f'{answer_1}{answer}')
                    z = 'T' #check answer code run
                else:
                    print(Fore.RED +messages['err-num']+color_reset)
                    z= "T"
        
                
            elif c in ['+', '-', '*', '**', '/', '//']: #if not match sqrt get b input form user
                b = None
                try:
                    b = float(input(messages['in-num2']+dot+color_reset ))
                except:
                    print(Fore.RED +messages['err-num']+color_reset)
                    #again()
                    #print("test?")
                           
                b = str(b) #change type
                a = str(a) #change type
           #change type
                
            else:
               # print("test?")
                z = 'T'
            #c = str(c) 
            

      #1anti-bug
            
    except:
        winsound.MessageBeep(winsound.MB_ICONHAND)#sound
        print(Fore.RED +messages['err-num']+color_reset) #consol message
        #message-box
        ctypes.windll.user32.MessageBoxW(0, "Please enter number", "Not Correct", 0 | 0x30)
        z = 'T'
        #print("test?s")
        #cal()#again run main code
    #    cal()
    if c in ['/', '//'] and b == '0':# #check b value is 0 
        print(Fore.RED +messages['err-num']+color_reset)
       # print("testtt")
    #2anti-bug
    try:
        #check for c value true
        #b = int(b)
       # if b == '0' and c in ['/', '//']:
       #      print(messages['err-num'])
                  
        if c in ['+', '-', '*', '**', '/', '//']:
            try:
                #b = str(b)
                answer = eval(a + c + b) #eval mathematical operations 
                print(f'{answer_1}{answer}')
                z = 'T'   #check answer code run 
            except:
                print(Fore.RED +messages['err-num']+color_reset)
                z = 'T'
             

        elif c in ["sqrt", None]: #its for dont bug else system
            c = '' #just for else work  

           
            #anti-bug
        else :
            print(Fore.RED +messages['err-operations'])#consol message
              
        z = 'T'   #check answer code run     
        
    #2anti-bug        
    except: 
        print(Fore.RED +messages['err-num']+color_reset)#consol message invalid number
        winsound.MessageBeep(winsound.MB_ICONHAND)#sound
        z = "T"
        #again()
        #message-box
        ctypes.windll.user32.MessageBoxW(0, "Please enter number!", "Not Correct", 0 | 0x30) 
       # cal()#again run main code
    if z == 'T' :#check answer code run
                check = 1 
                z = ''

    if check == 1 : #check answer code run       
    #if main code end ask user relaunch
        again()
        check = 0 #reset value   



#relaunch code


def again():
    rep = None  #reset value
    try: 
        time.sleep(1)
        rep = str(input(Fore.LIGHTRED_EX +"\n"+messages['relaunch']+dot+color_reset))#user answer input
        print(Fore.RESET +"") #for color reset with answer user
        if rep == "y" :   #check user answer
            time.sleep(2)
            cal()#relaunch main code
            
            
        elif rep == "n" :   #check user answer
            print(messages['5s'])    
            def end():#start fake end time
    #fake-end-time           
                print(messages['0s'])
                time.sleep(1)
                exit()
            
            t = Timer(5.0, end)#after 5 s end app
            t.start() #start timer  
        
#anti-bug     
        else :
            time.sleep(2)
            print(Fore.LIGHTRED_EX +messages['invalid-value']+color_reset) 
            again()
    except:
       time.sleep(2)
       print(Fore.LIGHTRED_EX +messages['invalid-value']+color_reset)
       again() 
m = 1 
     
#call main code . at the first lunch app this code work   
if m == 1:
    cal()
    m = 0#reset value    
   
    
