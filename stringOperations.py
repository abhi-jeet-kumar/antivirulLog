import re
import json
import sys

msg = sys.stdin.read()

key = []
value = []
msg_val_temp = re.findall(r'(?<=msg=)(.*)(?=\W\n)' , msg , re.MULTILINE)
for i in msg_val_temp:
    if len(i)!=0:
        msg_val = i

newMsgString = msg.replace('|','| ').replace(' ' , ' \n')        


temp_key = re.findall(r'(^\S\w+(?==))' , newMsgString , re.MULTILINE)
for i in temp_key:
    key.append(i)
newMsgString = newMsgString.ljust(len(newMsgString)+1)
temp_value = re.findall(r'(?<=\w=)(.*?)(?=\s)' , newMsgString , re.MULTILINE)
for j in temp_value:
    value.append(j)
for i in value:
    if i in msg_val:
        value[value.index(i)]=msg_val
keyValueDictionary = {k : v for k, v in zip(key, value)}
print(json.dumps(keyValueDictionary,indent=4))