list = [6,5,12,10,9,1,7,3]

print("This is an unsorted list:", list)

def merge(list):
    if len(list) > 1:
        mp = len(list)//2
        L = list[:mp]
        R = list[mp:]
        merge(L)
        merge(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1

def display(list):
    for i in range(len(list)):
        print(list[i], end =  " ")
    print()

merge(list)
print("This is the sorted list:")
display(list)