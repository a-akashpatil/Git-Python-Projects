import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    try:
        seconds = int(input("Enter the number of seconds to countdown: "))
        countdown_timer(seconds)
    except ValueError:
        print("Invalid input. Please enter a valid number of seconds.")
