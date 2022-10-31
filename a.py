import os,platform

riki=platform.architecture()[0]

os.system('git pull')

if riki=="64bit":
    print('Your Phone is 64 bit')
    __import__("SEXY").mahadi143()

elif riki=="32bit":
    print('Sorry Unsupported Device..!')
