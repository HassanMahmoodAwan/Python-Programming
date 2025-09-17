import os
import time
import subprocess
import sys
from datetime import datetime

def os_module():
    os.getcwd()
    os.path.abspath("./")   # Same as Upper, empty through Error.
    print(os.path.abspath(__file__))    # File abs Path
    
    os.path.isfile("./12-FileHandling_Sys_dateTime.py")  # True
    os.path.exists("E:\MEDIA\HASSAN")               # True
    os.mkdir(
        os.path.join(os.getcwd(), "TempDir")
        )
    os.rename("TempDir", "changed Name")
    os.rmdir("./changed Name")
    
    print(os.listdir())
    
    

def file_handling():
    file  = open("tempfile.txt", "x")        # Empty File creation, if already exist gives Error.
    file.close()
    
    with open("tempfile.txt", "w") as f:
        f.write("Hello World. I am learning Python!")
        f.close()

    with open("tempfile.txt", "a") as f:
        f.write("\nAdded Text")
        
    with open("tempfile.txt", "r") as f:
        data = f.read()
        f.close()
    
    time.sleep(5)
    os.remove("./tempfile.txt")
            
    print(data)    
    

def sys_module():
    subprocess.run([sys.executable, "03-Strings.py"])
     
    print(sys.version)          # 3.13.7
    print(sys.executable)       # Python path/
    print(sys.platform)         # returns win32
    print(sys.argv)             # args pass when running script. returns  ['.\\12-FileHandling_Sys_dateTime.py', 'Hello world']
     
    
    sys.exit(0)             # Exist with success
    # sys.exit(1)           # Exist with Error.


def datetime_module() -> None:
    now = datetime.now()       # Current Time
    print(
        now,
        now.date(),
        now.time(),
        now.today(),        # same as now
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second,
        now.microsecond)
    
    myFormatTime = now.strftime("%H-%S-%M and  %Y %B %A %a %b")  # 16-44-31 and  2025 September Wednesday Wed Sep
    print(myFormatTime)



if __name__ == "__main__":
    # os_module()
    # file_handling()
    # sys_module()
    datetime_module()
    