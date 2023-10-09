import time
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.pswd import real_password

def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password():
    pass # return cracked password
