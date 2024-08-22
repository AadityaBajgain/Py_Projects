import time

def countdown(duration):
    while duration > 0:
        print(f" {duration}")
        time.sleep(1)  #stops for 1 sec
        duration-=1

def main():
    try:
        countdown_duration = int(input("Duration of countdown: "))
        if countdown_duration > 0:
            countdown(countdown_duration)
            print("time's off, countdown finished!!")
        else:
            print("enter the positive integer")
    except ValueError:
        print("invalid input. Enter the positive integer!!")
    
if __name__=="__main__":
    main()
