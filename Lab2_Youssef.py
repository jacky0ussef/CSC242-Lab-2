'''
Jack Youssef
2/1/2023

This program holds a quicksort algorithm that leverages insertion sort for lists with less than 10 items.

Summary:
   - For a list of 20 items, quicksort took an average of 90 comparisons and 60 exchanges.
   - This list length took an average of 105 comparisons and 105 Exchanges. Both methods took <0.0 seconds to execute. Thus, 20 items is more efficient with quicksort.
   - For a list of 10 items, quicksort took an average of 33 and 35 comparisons and exchanges, respectively. 
   - This list length took an average of 24 and 25 exchanges for comparisons and exchanges, respectively. The time was again negligible for this set size.
   - Thus, I found insertion sort to be faster for smaller sets only at lists with an average of <=10 items. 
   - For my conditions and equipment, the best threshold was 10 items for using insertion sort.
'''


import random
from profiler import Profiler

def quicksort(lyst, profiler):
    if len(lyst) <= 10:
        insertionSort(lyst, profiler)
    else:
        quicksortHelper(lyst, 0, len(lyst) - 1, profiler)

def quicksortHelper(lyst, left, right, profiler):
    profiler.comparison()
    if left < right:
        pivotLocation = partition(lyst, left, right, profiler)
        quicksortHelper(lyst, left, pivotLocation - 1, profiler)
        quicksortHelper(lyst, pivotLocation + 1, right, profiler)

def partition(lyst, left, right, profiler):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    profiler.exchange()
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        profiler.comparison()
        if lyst[index] < pivot:
            swap(lyst, index, boundary, profiler)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap (lyst, right, boundary, profiler)
    return boundary

def swap(lyst, i, j, profiler):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
    profiler.exchange()

def insertionSort(lyst, profiler):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            profiler.comparison()
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                profiler.exchange()
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        profiler.exchange()
        i += 1

def main(size = 10, sort = quicksort):
    lyst = []
    p = Profiler()
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    p.test(sort, lyst, size, unique = True, comp = True, exch = True, trace = False)
    
if __name__ == "__main__":
    main()
    
    
    