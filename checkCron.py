#!/usr/bin/env python3

import re
import sys
import shutil
from shutil import copyfile

src= '/var/log/syslog'
dst = '/home/sonali/projects/cronLogCheck/syslog'

shutil.copyfile(src, dst)

logFile = sys.argv[1]
with open(logFile) as f:
    for line in f:
        if 'CRON' not in line:
            continue 
        pattern =r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        print(result)