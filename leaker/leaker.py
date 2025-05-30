import time
import requests
import random

print("running leaker.py")
suspicious_targets = [
    "http://45.77.23.19:8080",
    "http://93.184.216.34:9000",  # example.com
    "http://198.51.100.42:1234"
]
 
while True:
    target = random.choice(suspicious_targets)
    try:
        print(f" Attempting to exfiltrate to {target}")
        requests.get(target)
    except Exception as e:
        print(" Blocked or failed:", e)
    time.sleep(10)