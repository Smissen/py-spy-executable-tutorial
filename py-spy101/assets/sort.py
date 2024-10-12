import random
import time
import sys

# O(n) if you're lucky! :)
def bogosort(arr):
    while True:
        if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
            return arr
        random.shuffle(arr)

# Now this is quick!
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    elif len(arr) <= 9:
        return bogosort(arr)
    elif len(arr) > 10000 and len(arr) < 100000:
        snorlax()
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

# This guy is always in the way!
def snorlax():
    for _ in range(random.randint(10, 15)):
        for n in range(999999999999999):
            n = n +1
        print("zzzZZZzzz")

# Don't touch :#
arr = [random.randint(0, 100000) for _ in range(int(sys.argv[1]))]

print("Sorted array:", quicksort(arr))