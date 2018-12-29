# -*- coding: utf-8 -*-
import os
import time
import sys
import random
print("Loading...")
print("Loading Config...")
import config, re
from Tkinter import Tk
from tkinter.filedialog import askopenfilename

config_file="Code_Convert.conf"
out=config.process(config_file)
keys=out[0]
values=out[1]
x=-1
codes={}
version=0.1
QUIET="False"
def wait():
        try:
                global WAIT_TIME
                time.sleep(float(WAIT_TIME))
        except:pass
for dat in  keys:
        x=x+1
        wait()
        if QUIET=="False":
                if values[x]=="True":
                        print("Enabling Mod: "+str(dat))
                elif values[x]=="False":
                        print("Disabling Mod: "+str(dat))
                else:
                        print("Setting key: "+str(dat)+" to value: "+str(values[x]))
        exec(dat +" ='"+str(values[x])+"'")
class Library_Tools():
        def __init__(self):
                global LIBRARY, codes
                self.errors=[]

        def Reset_Library(self):
                global LIBRARY,codes
                codes={}
                
        def Load_Library(self):
                global LIBRARY, codes
                used=[]
                try:
                
                    wait()
                    print(">>Loading Library")
                    if not LIBRARY=="Built-in":
                        wait()
                        out=config.process(LIBRARY)
                        letters=out[0]
                        code_out=out[1]
                        x=-1
                        for dat in letters:
                            x=x+1
                            wait()
                            print(">>>>LOADING:"+str(dat)+":"+str(code_out[x]))
                            codes[dat]=code_out[x]
                            print(">>>>OK!")           
                    else:
                        wait()
                        raise SystemError()#Throw an error on purpose to make less programming! :)
                        raw_input("How did you get this far!? Python should crash here!")
                    print(">>Library Loaded: "+str(LIBRARY))
                except:
                    print(">>>>No external library requested... Loading Built-In..")
                    codes={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....",
                       "I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.",
                       "S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","~":" ","0":"-----","1":".----","2":"..---","3":"...--",
                       "4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-",",":"--..--","?":"..--..","/":"-..-.","@":".--.-.","[?]":"??","CODE":"BI"}
                    print(">>OK!")
                    wait()
                rtn=self.Check_Library()
                unrecov=False
                if "HEALTHY" in rtn:
                        print("No Issues Found!")
                else:
                        print("Warning: an issue was detected with the loaded code file:\n\n")
                        for item in rtn:
                                print(">> "+item+"\n")
                                if "Unrecoverable" in item:
                                        unrecov=True
                        if unrecov==True:
                                print("\n\n These errors are unrecoverable! Please re-load or load a different code before attempting to use the system")
                        else:
                                print("\n\nThe system has recovered from these errors. You may continue using the code system as normal.")
                        raw_input("\n press enter to continue")

                        
        def Check_Library(self):
                global LIBRARY, codes
                used=[]
                used2=[]
                self.errors=[]
                print("Checking Library: ")
                x=-1
                stat="HEALTHY"
                for item in codes:
                    x=x+1
                    wait()
                    print(item+">>"+codes[item])
                    if item in used:
                            print("WARNING: Duplicate Character was found!")
                            stat="Duplicate Character was found! (Unrecoverable)"
                            self.errors.append(stat)
                    else:
                        used.append(item)
                    if codes[item] in used2:
                            print("WARNING: Duplicate Character was found!")
                            stat="Duplicate Character was found! (Unrecoverable)"
                            self.errors.append(stat)
                            break;
                    else:
                            used2.append(codes[item])
                if not "~" in codes:
                    codes["~"]=" "
                if not "[?]" in codes:
                    print(">>>>WARNING: No or incorrect unknown character given. Adding [?]  to database")
                    codes["[?]"]="??"
                    print(">>>>OK!")
                if not "CODE" in codes:
                    print(">>>>WARNING: No code in database")
                   
                    stat="No Code in database (Unrecoverable)"
                    self.errors.append(stat)
                Library_Tools.Length_Of_Library=x
                if stat=="HEALTHY":
                        return "HEALTHY"
                else:
                        return self.errors
lib=Library_Tools()
lib.Load_Library()

wait()
print("Total Length of Library: "+str(Library_Tools.Length_Of_Library))
wait()
try:
        if SILENT_START=="True":
                os.system("cls")
except:
        pass
print("WELCOME TO THE CODE CONVERSION ENGINE!")

try:
        if QUICK_START=="False":
                raw_input("Press Enter to Begin!")
except:
        raw_input("Press Enter to Begin!")
class converter():
    global codes
    def __init__(self):
        self.test=""
    def English_To_Morse(self,inputs):
        output=codes["CODE"]
        print("Converting: "+str(inputs)+" to morse")
        inputs=inputs.replace(" ","~")#Make sure
        pre_convert=list(inputs)
        for item in pre_convert:
            if item.upper() in codes:
                    print(codes[item.upper()])
                    output=output+"/"+codes[item.upper()]
            else:
                    print("No Conversion Data found for Character: "+str(item))
                    output=output+"/"+codes["[?]"]
                    
        return output
    def Morse_To_English(self, inputs):
        inputs=inputs.replace("\n","/")
        if not codes["CODE"] in inputs:
                return "The conversion failed because the incorrect library was loaded"
        else:
                pre_convert=re.split(r"/",inputs)
                output=""
                for items in pre_convert:
                        for thing in codes:
                                if items==codes[thing]:
                                        print(items+">>"+thing)
                                        output=output+thing
                                        break;
        output=output.replace("~"," ")
        output=output.replace("CODE","")
        return output
while True:
    os.system("cls")
    print("Code Conversion Engine Version "+str(version))
    print("\n\n[0] Code >> English\n[1] English >> Code\n[2] Generate Random Code\n[3] Load Library")
    sel=raw_input("Select an option: ")
    if sel=="0":
        inp=raw_input("Please enter something to translate with / as a seperating character: ")
        convert=converter()
        converted=convert.Morse_To_English(inp)
        os.system("cls")
        if not "failed" in converted:
                
                print("Here's the converted string: ")
        if "[?]" in converted:
                print("Some Characters were not able to be translated and are noted by [?]\n\n")
        print("\n\n\n\n"+str(converted))
        
        raw_input("\n\n\n\nPress Enter to return")
    elif sel=="1":
        inp=raw_input("Please enter something to translate: ")
        convert=converter()
        converted=convert.English_To_Morse(inp)
        os.system("cls")
        print("Here's the converted string: ")
        if "/??/" in converted or "/??" in converted:
                print("Some Characters were not able to be translated and are noted by /??/\n\n")
        print("\n\n\n\n"+str(converted))
        raw_input("\n\n\n\nPress Enter to return")
    elif sel=="2":
        name=raw_input("Please enter a name for this code: ")
        name=name+".txt"
        chars=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","<",">","?",".",",",";","'",":","[","]","{","}","=","-","_","+"]
        print("Generating Random Code...")
        used=[]
        open(name,"w+").write("")
        rand=random.choice(chars)

        for item in chars:
                while rand in used:
                        rand=random.choice(chars)
                used.append(rand)
                print(str(item)+">>"+str(rand))
                open(name,"a").write(str(item)+"="+str(rand)+"\n")
        open(name,"a").write(" =~\n[?]=??\nCODE=="+str(random.random()))
        print("Done... Saved as: "+str(name))
        ques=raw_input("Would you like to load this code into the converter? (y/n)")
        if "Y" in ques.upper():
                print("Loading...")
                LIBRARY=name
                lib.Reset_Library()
                lib.Load_Library()
        
    elif sel=="3":
        print("Please enter a file to load: ")
        Tk().withdraw()
        filename = askopenfilename()
        LIBRARY=filename
        print(LIBRARY)
        lib.Reset_Library()
        lib.Load_Library()
        raw_input("Press enter")
