import time
import requests
 
while True:
    try:
        print(" Sending logs to internal log server...")
        requests.post("http://log-server/logs", json={"msg": "reporter active"})
    except Exception as e:
        print("Failed to send logs:", e)
    time.sleep(15)
 