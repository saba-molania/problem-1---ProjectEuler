# Loop back to this point once code finishes

loop = 1
while (loop < 10):
    # All the questions that the program asks the user
    city = input("Choose a city :\t")
    name = input("Choose a girl name :\t")
    adjective = input("Coose an adjective :\t")
    infinitive = input("Choose an infinitive :\t")
    adjective2 = input("Choose an adjective :\t")

    # Displays the story based on the users input

    print("----------------------------------------")
    print("Angela and Tom live in",city)
    print("Angela's sister",name,"lives in",city)
    print("Angela and Tom are",adjective)
    print(name,"sits by Angella")
    print("Angela sits by Tom")
    print("Angella and Tom want",infinitive)
    print("Angela and Tom go to the yard")
    print("Angela and Tom jump and yell")
    print("Angela and Tom sing and run")
    print("Angela and Tom are",adjective)
    print("Angela and Tom stop")
    print("Angela and Tom are",adjective2)
    print("----------------------------------------")

# Loop back to "loop = 1"
loop = loop + 1