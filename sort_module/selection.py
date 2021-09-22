def selectionSort(array):
    for i in range(len(array)):
        minindex = i
        for j in range(i + 1, len(array)):
            if array[minindex] > array[j]:
                minindex = j
        array[i], array[minindex] = array[minindex], array[i]       