import subprocess
import time

def update(command1):
    print("******************** UPDATING ********************")
    subprocess.call(command1, shell=True)

def upgrade(command2):
    print("******************** UPDATING ********************")
    subprocess.call(command2, shell=True)

def clear(command3):
    print("********** CLEARING **********")
    subprocess.call(command3, shell=True)

try:
    update('sudo apt update')
    time.sleep(5)

    upgrade('sudo apt upgrade')
    time.sleep(4)

except Exception as error1:
    print(error1)

ans = input("Would you like to 'clear' current terminal window? >>: ")
try:
    if ans == 'yes':
        clear('clear')
    
    elif ans == 'no':
        print(':) :) !Goodbye! :) :)')

except Exception as error2:
    print(error2)
    