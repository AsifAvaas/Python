import requests
from datetime import datetime
import time


def timeFormat(start_time):
    readable_time = datetime.utcfromtimestamp(start_time)
    formatted_time = readable_time.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_time


base_url='https://kenkoooo.com/atcoder/resources/contests.json'

response=requests.get(base_url)
data=response.json()
# print(data[0])
current_time=int(time.time())
for line in data:
    start_time=line['start_epoch_second']
    if current_time<start_time:
        print(line['title'])
    
# print(len(data))
# print(data[1320])
# print(timeFormat(data[1320]['start_epoch_second']))
# print(current_time>data[1320]['start_epoch_second'])
