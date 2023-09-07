# Import Time Module
import time

# Get Seconds From User Input
seconds = input("Enter Time In Seconds: ")

# Define CounterTime Function
def countDown(seconds):
    while seconds > 0:
        mins = int(seconds / 60)
        secs = int(seconds % 60)
        timer = f"{mins}:{secs}"
        print(timer)
        seconds -= 1
    print("Time's Up")
countDown(int(seconds))