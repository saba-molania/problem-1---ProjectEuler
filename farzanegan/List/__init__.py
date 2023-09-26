def bubble_sort(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]
    return l


