import time
from os import system,name
while True :
    choice = input("\nDo you want to start? (y/n) :\t")
    if "y" in choice.lower() :
        hour = int(input("\nEnter amount of hour :\t"))
        minutes = int(input("Enter amount of minutes :\t"))
        seconds = int(input("Enter amount of seconds :\t"))
        total = hour*60*60+minutes*60+seconds
        print("\nTimer starts now...")
        time.sleep(1)
        while total >= 1 :
            print(total)
            total -= 1
            time.sleep(1)
            if name == "nt" :
                system("cls")
            else:
                system("clear")
        print("Timer ended...")
    elif "n" in choice.lower() :
        print("\nExiting...")
        break
    else:
        print("\nInvalid input...")