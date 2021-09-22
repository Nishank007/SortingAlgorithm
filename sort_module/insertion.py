def InsertionSort(array):
    for i in range(1, len(array)):
        k = array[i]
        j = i - 1
        while j >= 0 and k < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = k