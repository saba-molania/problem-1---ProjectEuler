# Bubble sort

def bubble_sort(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]
    return l

l=[21, 87, 76, 65, 54, 43, 32, 21, 90, 89, 102, 45, 13]

print(bubble_sort(l))
