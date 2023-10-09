import time
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.pswd import real_password

PASSWORD_LENGTH = 4
SECONDS_TO_CHECK_ONE_DIGIT = 0.1
POSSIBLE_VALUES_FOR_DIGIT = ["0","1","2","3","4","5","6","7","8","9"]

def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def check_combination(password, index, digit):
    password[index] = digit
    return check_password("".join(password))

def crack_password():
    password = ["0", "0", "0", "0"]
    for index in range(PASSWORD_LENGTH):
        for digit in POSSIBLE_VALUES_FOR_DIGIT:
            start_time = time.time()
            result = check_combination(password, index, digit)
            end_time = time.time()
            total_time = end_time - start_time
            if result == True:
                return "".join(password)
            if (SECONDS_TO_CHECK_ONE_DIGIT * (index + 2)) <= total_time <= (SECONDS_TO_CHECK_ONE_DIGIT * (index + 3)):
                break
