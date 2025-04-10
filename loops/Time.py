#doubles the wait time between retries, start from one but stops after 5 retries
import time 

waittime=1 
max_retries=5
attempt=0

while attempt < max_retries:
    print("Attempts ",attempt +1 ,"waittime ",waittime)
    time.sleep(waittime)
    waittime *=2
    attempt +=1



