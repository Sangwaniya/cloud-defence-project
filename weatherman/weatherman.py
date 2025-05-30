import time
import requests
 
while True:
    try:
        print("Fetching weather from trusted API...")
        res = requests.get("https://wttr.in/?format=3")
        print("📡 Weather:", res.text)
    except Exception as e:
        print("Failed to get weather:", e)
    time.sleep(20)