import psutil
import time
from datetime import datetime


def checkIfProcessRunning(processName):
    """
    Check if there is any running process that contains the given name processName.
    """
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


print("--------OSU!LAZER LOGS--------")
try:
    while True:
        if checkIfProcessRunning("dotnet"):
            print(f"{datetime.now()}: OSU!LAZER IS RUNNING.")
            while checkIfProcessRunning("dotnet"):
                time.sleep(0.6)
        else:
            print(f"{datetime.now()}: OSU!LAZER IS NOT RUNNING")
            while not checkIfProcessRunning("dotnet"):
                time.sleep(0.6)
except KeyboardInterrupt:
    pass
