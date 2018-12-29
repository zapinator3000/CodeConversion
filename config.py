#!/usr/bin/python
#This is the Configuration system for the New "Live" Game Console
import os
import time
import re
keys=[]
values=[]
def process(cnfg):
    global keys
    global values
    print("Reading Configuration...")
    config=re.split(r"\n", open(cnfg,"r").read())
    for item in config:
        if not item==" " and not item=="":
            if not item[0]=="#" and not item[0]==" " and not item[0]=="":
                splits=item.split("=",1)
            #print("Keys: "+str(splits[0]))
            #print("value: "+str(splits[1]))
                values.append(splits[1])
                keys.append(splits[0])
    return keys,values
