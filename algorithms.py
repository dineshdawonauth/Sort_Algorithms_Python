# ====================================
#       Bubble Sort Algorithm
# ====================================

def bubbleSort(array):
    wasSwapped = False    # Check if 2 elements were swapped

    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] >= array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                wasSwapped = True
        print(array)

        if not wasSwapped:
            break

    return array


'''
arr = [100, 2342, 1, 0, 23, 50, -4, 44, -100]

VISUALISATION:  
[100, 1, 0, 23, 50, -4, 44, -100, 2342]
[1, 0, 23, 50, -4, 44, -100, 100, 2342]
[0, 1, 23, -4, 44, -100, 50, 100, 2342]
[0, 1, -4, 23, -100, 44, 50, 100, 2342]
[0, -4, 1, -100, 23, 44, 50, 100, 2342]
[-4, 0, -100, 1, 23, 44, 50, 100, 2342]
[-4, -100, 0, 1, 23, 44, 50, 100, 2342]
[-100, -4, 0, 1, 23, 44, 50, 100, 2342]
[-100, -4, 0, 1, 23, 44, 50, 100, 2342]
[-100, -4, 0, 1, 23, 44, 50, 100, 2342]
'''



# ====================================
#       Quick Sort Algorithm
# ====================================

def quickSort(array, marker_1, marker_2):
    if marker_1 < marker_2:
        middle = partition(array, marker_1, marker_2)

        quickSort(array, marker_1, middle - 1)
        quickSort(array, middle + 1, marker_2)

    return array


def partition(array, marker_1, marker_2):
    i = marker_1 - 1
    pivot = array[marker_2]

    for j in range(marker_1, marker_2):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            print(array)

    array[i+1], array[marker_2] = array[marker_2], array[i+1]
    return (i+1)


'''
arr = [100, 2342, 1, 0, 23, 50, -4, 44, -100]

VISUALISATION: 
[-100, 1, 2342, 0, 23, 50, -4, 44, 100]
[-100, 1, 0, 2342, 23, 50, -4, 44, 100]
[-100, 1, 0, 23, 2342, 50, -4, 44, 100]
[-100, 1, 0, 23, 50, 2342, -4, 44, 100]
[-100, 1, 0, 23, 50, -4, 2342, 44, 100]
[-100, 1, 0, 23, 50, -4, 44, 2342, 100]
[-100, 1, 0, 23, 50, -4, 44, 100, 2342]
[-100, 1, 0, 23, 50, -4, 44, 100, 2342]
[-100, 1, 0, 23, 50, -4, 44, 100, 2342]
[-100, 1, 0, 23, -4, 50, 44, 100, 2342]
[-100, -4, 0, 23, 1, 44, 50, 100, 2342]
'''

# ====================================
#       Merge Sort Algorithm
# ====================================

def mergeSort(array):
    if len(array) > 1:
        midpt = len(array) // 2      # Find Midpoint
        right = array[midpt:]
        left = array[:midpt]

        mergeSort(right)
        mergeSort(left)

        i = j = k = 0  # Initialize Counters

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
            # print(array)

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array
