import os
import re
import json
key = []
value = []
msg_val = ''

#function to extract message value
def msgValueExtractor(r):
    for line in r:
        msg_val_temp = re.findall(r'(?<=msg=)(.*)(?=\W\n)' , line , re.MULTILINE)
        for i in msg_val_temp:
            if len(i)!=0:
                return i

#function to extract required key value pair
def keyValue(msg_val,data):
    temp_key = re.findall(r'(^\S\w+(?==))' , data , re.MULTILINE)
    for i in temp_key:
        key.append(i)
    data = data.ljust(len(data)+1)
    temp_value = re.findall(r'(?<=\w=)(.*?)(?=\s)' , data , re.MULTILINE)
    for j in temp_value:
        value.append(j)
    for i in value:
        if i in msg_val:
            value[value.index(i)]=msg_val
    return(key,value)
    


def driver_func():
    #to extract message value
    with open("antivirus_log.txt", "r") as r:
        msg_val=msgValueExtractor(r)

    #to create new log file
    with open("antivirus_log.txt", "r") as r:
        with open("newlogFile.txt", "w") as w:
            w.write(r.read().replace('|','| ').replace(' ' , ' \n'))
    
    #to store required key value pairs
    with open('newlogFile.txt','r') as file:
            data = file.read()
            key,value=keyValue(msg_val,data)

    #creating dictionary with key value pairs
    keyValueDictionary = {k : v for k, v in zip(key, value)}

    #dumping dictionary in a json file
    with open('keyValueOutput.json', 'w') as file:
        json.dump(keyValueDictionary,file, indent=4)
    
    #deleting new log file
    os.remove('newlogFile.txt')


driver_func()

        