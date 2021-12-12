# Write a program to process log messages and find total time required to complete the build process.

# datetime [level] message
# Sample Log messages
# 2020-11-30T09:43:49Z [info] Config: Interval:10s, Quiet:false, Hostname:"localhost", Flush Interval:10s
# 2020-11-30T09:44:09Z [error] When writing to [http://localhost:8086]: Post "http://localhost:8086/write?db=telegraf": dial tcp 127.0.0.1:8086: connect: connection refused
# 2020-11-30T09:44:10Z [warning] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory
# 2020-11-30T09:44:20Z [error] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory
#"2020-11-30T09:44:09Z [error] When writing to ['http://localhost:8086']: Post "http://localhost:8086/write?db=telegraf": dial tcp 127.0.0.1:8086: connect: connection refused",
import re
from datetime import datetime
start_time = ''
end_time = ''
new_log = []
log_list = [
  '2020-11-30T09:41:10Z [info] Success in plugin: success getting disk io info: open /proc/diskstats: no such file or CASS: Instance Deployment started directory',
  '2020-11-30T09:42:10Z [info] Deploying disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:43:49Z [info] CASS: Instance Deployment started.',
  '2020-11-30T09:43:49Z [info] Config: Interval:10s, Quiet:false, Hostname:"localhost", Flush Interval:10s.',
  '2020-11-30T09:44:09Z [error] When writing to ["http://localhost:8086": Post "http://localhost:8086": dial tcp 127.0.0.1:8086: connect: connection refused',
  '2020-11-30T09:44:10Z [warning] Error in plugin: warning getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:44:10Z [info] Deploying disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:45:10Z [info] CASS: Instance Deployment configured.',
  '2020-11-30T09:45:10Z [warning] Warning in plugin: error getting disk io info: open /proc/diskstats: no such file or directory.',
  '2020-11-30T09:45:20Z [error] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:54:10Z [info] CASS: Instance Deployment complete.'
  '2020-11-30T09:47:10Z [info] Info in plugin: error getting disk io info: open /proc/diskstats: no such file or directory in Instance Deployment complete in progress'
  '2020-11-30T09:49:10Z [error] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory'
  '2020-11-30T09:51:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:54:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:55:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:57:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory'
]

#create a new log list with new lines
for i in log_list:
  switch = re.findall(r'\d{4}-\d{2}-\d{2}',i)
  for x in switch:
    new_log.extend(i.replace(x,'\n{}'.format(x)).splitlines())




#parsing the new log list
for i in new_log:
  if 'Instance Deployment started.' in i:
    for x in (re.findall(r'\d{4}-\d{2}-\d{2}',i)):
      date = x
    for y in (re.findall(r'\d{2}:\d{2}:\d{2}',i)):
      time = y
    start_time = '{} {}'.format(date,time)
  if 'CASS: Instance Deployment complete.' in i:
    for x in (re.findall(r'\d{4}-\d{2}-\d{2}',i)):
      date = x
    for y in (re.findall( r'\d{2}:\d{2}:\d{2}',i)):
      time = y
    end_time = '{} {}'.format(date,time)
            
            
            
#difference calculator
startTimeStamp = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
endTimeSTamp = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

if startTimeStamp > endTimeSTamp:
    timeDifference = startTimeStamp - endTimeSTamp
else:
    timeDifference = endTimeSTamp - startTimeStamp
timeDifference_mins = int((timeDifference.total_seconds() / 60))
timeDifference_secs = int((timeDifference.total_seconds() % 60))


print('Total time taken is {} minutes and {} seconds'.format(timeDifference_mins,timeDifference_secs))