import re, os, datetime

filename = 'e:\output_1981.10.21.txt'
if os.path.exists(filename) == False:
    print(filename,"file make!")
    fp = open(filename,'w+')
    fp.close()

replace_name = re.search('(?P<year>\d{4}.\d{2}.\d{2}.)', filename)
format_str = 'e:\output_%Y.%m.%d.txt'
date_fix = datetime.datetime.strptime(filename, format_str)
week = date_fix.isoweekday()
fix_name = 'e:\output_'+ replace_name.group(0) + str(week) + '.txt'
print(fix_name)
os.rename(filename,fix_name)

'''
use fortmat_str,strptime,isoweekday
datetime
'''