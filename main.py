import os
import requests
import time
import csv

url="https://cloud.timeedit.net/chalmers/web/public/ri1Yf3ygZ05ZZfQ1X75v5Yn75Z45x4Z6Qg080YQQ6176bQo0QyX.csv"



with requests.Session() as s:
    download = s.get(url)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)

if time.strftime("%Y-%m-%d") == my_list[4][0]:
    a=int(time.strftime("%H"))
    b=int(time.strftime("%M"))
    c = int(my_list[4][1][0:2])
    d = (int(my_list[4][1][3:5])-15)
    timeDone = c*60+d+15
    if d < 0:
        c = c - 1
    d = d % 60


    timeNow = a*60+b
    timeLesson = c*60+d
    
    if timeLesson - timeNow < 0 and timeNow - timeDone < 0:
        cmd = 'notify-send -u normal "' + my_list[4][4] + ' börjar snart"'
        os.system(cmd)
