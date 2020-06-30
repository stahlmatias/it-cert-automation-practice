#!/usr/bin/env python3

import csv
import re
import operator

error_dict = {}
user_dict = {}
error = 0
info = 0
syslog_file = 'syslog.log'

try:
  fp = open(syslog_file)
  line = fp.readline()
  while line:
    error_msg = re.search(r"ticky: ERROR (.*) \((.*)\)", line)
    info_msg = re.search(r"ticky: INFO (.*) \((.*)\)", line)
    if error_msg:
      if error_msg.group(1) not in error_dict.keys():
        error_dict[error_msg.group(1)] = 1
      else:
        error_dict[error_msg.group(1)] += 1
      if error_msg.group(2) not in user_dict.keys():
        error = 1
        user_dict[error_msg.group(2)] = [info,error]
      else:
        error = error + 1
        user_dict[error_msg.group(2)] = [info,error]
    if info_msg: 
      if info_msg.group(1) not in user_dict.keys():
        info = 1
        user_dict[info_msg.group(1)] = [info,error]
      else:
        info = info + 1
        user_dict[info_msg.group(1)] = [info,error]
    line = fp.readline()
  sorted(error_dict.items(), key=operator.itemgetter(0))
except:
  fp.close()

error_file = open('error_message.csv', 'w')
user_stats_file = open('user_statistics.csv', 'w')

error_header = "Error, Count\n"
user_stats_header = "Username, INFO, ERROR\n"

error_file.write(error_header)
for error, count in error_dict.items():
  line = ("{error}, {count}\n".format(error=error, count=count))
  error_file.write(line)
error_file.close()

user_stats_file.write(user_stats_header)
for username, stats in user_dict.items():
  line = ("{username}, {INFO}, {ERROR}\n".format(username=username, INFO=stats[0],ERROR=stats[1]))
  user_stats_file.write(line)
user_stats_file.close()

