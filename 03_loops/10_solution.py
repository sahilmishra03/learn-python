import time

wait_time=1
attempts=0
max_try=5

while attempts<max_try:
    print("Wait Time -",wait_time,"Attempt -",attempts+1)
    time.sleep(wait_time)
    wait_time=wait_time*2
    attempts=attempts+1