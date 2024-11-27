import requests
import hashlib
import random
import time
from datetime import datetime
from dotenv import load_dotenv
import os



def timeFormat(start_time):
    readable_time = datetime.utcfromtimestamp(start_time)
    formatted_time = readable_time.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_time


load_dotenv()
key=os.getenv('CODE_FORCES_API_KEY')
secret=os.getenv('CODE_FORCES_API_SECRET')



rand=str(random.randint(100000, 999999))
current_time=int(time.time())
method = "contest.list"
base_url = "https://codeforces.com/api"

def generate_api_request(api_key, secret, rand, method, base_url):
    current_time = int(time.time())
    
    # Query parameters
    params = {
        "gym": 'false',
        "apiKey": api_key,
        "time": current_time,

    }
    
    # Step 1: Sort parameters lexicographically by key
    sorted_params = "&".join(f"{key}={value}" for key, value in sorted(params.items()))
    
    # Step 2: Construct the base string for hashing
    base_string = f"{rand}/{method}?{sorted_params}#{secret}"
    
    # Step 3: Compute the SHA-512 hash
    hash_object = hashlib.sha512(base_string.encode('utf-8'))
    hash_hex = hash_object.hexdigest()
    
    # Step 4: Construct the full API signature
    api_sig = f"{rand}{hash_hex}"
    
    # Step 5: Build the full API request URL
    full_url = f"{base_url}/{method}?{sorted_params}&apiSig={api_sig}"
    return full_url

params = {
    "contestId": 566,
    "apiKey": key,
    "time": current_time,

}
hashData=generate_api_request(key,secret,rand,method,base_url)
# print(hashData)
result= requests.post(hashData)
data=result.json()

# print(data['result'][0])

for i in range(10,-1,-1):
    if data['result'][i]['relativeTimeSeconds']<0:
        print(data['result'][i]['name'])
        start_time=timeFormat(data['result'][i]['startTimeSeconds'])
        print(start_time)
        id=data['result'][i]['id']
        print(f"Click to register: https://codeforces.com/contestRegistration/{id}")

        print('\n')

# {'id': 2034, 'name': 'Rayan Programming Contest 2024 - Selection (Codeforces Round, Div. 1 + Div. 2)', 'type': 'CF', 'phase': 'BEFORE', 'frozen': False, 'durationSeconds': 10800, 'startTimeSeconds': 1732977300, 'relativeTimeSeconds': -354354}