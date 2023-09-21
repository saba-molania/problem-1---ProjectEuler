import time
from os import system,name


def clear():
    if name == "nt" :
        system("cls")
    else:
        system("clear")
        return name
    

def total(hour,minutes,seconds):
    t = hour*60*60+minutes*60+seconds
    return t


def get_time_from_user():
    hour = int(input("\nEnter amount of hour :\t"))
    minutes = int(input("Enter amount of minutes :\t"))
    seconds = int(input("Enter amount of seconds :\t"))
    t = total(hour,minutes,seconds)
    return t


def output(t):
    while t >= 1 :
        print(t)
        t -= 1
        time.sleep(1)
        clear()
    return t

def main():
    while True :
        choice = input("\nDo you want to start? (y/n) :\t")
        if choice.lower() in ["y","yes"]:
            t = get_time_from_user()
            print("\nTimer starts now...")
            time.sleep(1)
            output(t)
            print("Timer ended...")
        elif choice.lower() in ["n","no"] :
            print("\nExiting...")
            break
        else:
            print("\nInvalid input...")
main()