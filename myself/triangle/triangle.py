s = int(input(" enter a number :\t"))
for i in range(1,s,2):
    print((s-i)//2 * " " + i * "*")
