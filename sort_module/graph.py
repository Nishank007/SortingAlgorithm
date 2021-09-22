import numpy as np
import random
from numpy.random import seed
from numpy.random import randint
import timeit
import matplotlib.pyplot as plt

from sort_module import selection
from sort_module import bubble
from sort_module import heap
from sort_module import quick_median_sort
from sort_module import quick
from sort_module import merge
from sort_module import insertion

def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
print()
b_times = list()
b_elements = list()
m_times = list()
m_elements = list()
h_times = list()
h_elements = list()
i_times = list()
i_elements = list()
s_times = list()
s_elements = list()
q_times = list()
q_elements = list()
qr_times = list()
qr_elements = list()
print('\n')

def graph():
    print("Enter 4 large random numbers for each sorting algorithm")
    print("SELECTION SORT:-")
    for i in range(1, 5):
        n = int(input("Enter your large random number:- "))
        random_list = randint(0, n, n)
        print("Pseudo-Random Generated Array", end='\n')
        print(np.array2string(random_list, separator=', '))
        start = timeit.default_timer()
        selection.selectionSort(random_list)
        stop = timeit.default_timer()
        print("Sorted array:- ", end='\n')
        print(np.array2string(random_list, separator=', '))
        print(len(random_list), "Elements were sorted by Selection Sort in ", stop - start)
        s_elements.append(len(random_list))
        s_times.append(stop - start)
    print('\n')
    print("QUICK SORT:-")
    for i in range(1, 5):
        n = int(input("Enter your large random number:- "))
        random_list = randint(0, n, n)
        print("Pseudo-Random Generated Array", end='\n')
        print(np.array2string(random_list, separator=', '))
        start = timeit.default_timer()
        quick.quicksort(random_list, 0, n - 1)
        stop = timeit.default_timer()
        print("Sorted array:- ", end='\n')
        print(np.array2string(random_list, separator=', '))
        print(len(random_list), "Elements were sorted by Quick Sort in ", stop - start)
        q_elements.append(len(random_list))
        q_times.append(stop - start)
    print('\n')
    print("QUICK SORT USING 3 MEDIANS:-")
    for i in range(1, 5):
        n = int(input("Enter your large random number:- "))
        random_list = randint(0, n, n)
        print("Pseudo-Random Generated Array", end='\n')
        print(np.array2string(random_list, separator=', '))
        start = timeit.default_timer()
        quick_median_sort.quicksortmedian(random_list)
        stop = timeit.default_timer()
        print("Sorted array:- ", end='\n')
        print(np.array2string(random_list, separator=', '))
        print(len(random_list), "Elements were sorted by Quick Sort using 3 medians in ", stop - start)
        qr_elements.append(len(random_list))
        qr_times.append(stop - start)
    print('\n')
    print("BUBBLE SORT:-")
    for i in range(1, 5):
        n = int(input("Enter your large random number:- "))
        random_list = randint(0, n, n)
        print("Pseudo-Random Generated Array", end='\n')
        print(np.array2string(random_list, separator=', '))
        start = timeit.default_timer()
        bubble.bubbleSort(random_list)
        stop = timeit.default_timer()
        print("Sorted array:- ", end='\n')
        print(np.array2string(random_list, separator=', '))
        print(len(random_list), "Elements were sorted by Bubble Sort in ", stop - start)
        b_elements.append(len(random_list))
        b_times.append(stop - start)
    print('\n')
    print("MERGE SORT:-")
    for i in range(1, 5):
        n = int(input("Enter your large random number:- "))
        random_list = randint(0, n, n)
        print("Pseudo-Random Generated Array", end='\n')
        print(np.array2string(random_list, separator=', '))
        start = timeit.default_timer()
        merge.mergeSort(random_list)
        stop = timeit.default_timer()
        print("Sorted array:- ", end='\n')
        print(np.array2string(random_list, separator=', '))
        print(len(random_list), "Elements were sorted by Merge Sort in ", stop - start)
        m_elements.append(len(random_list))
        m_times.append(stop - start)
    print('\n')
    print("HEAP SORT:-")
    for i in range(1, 5):
        n = int(input("Enter your large random number:- "))
        random_list = randint(0, n, n)
        print("Pseudo-Random Generated Array", end='\n')
        print(np.array2string(random_list, separator=', '))
        start = timeit.default_timer()
        heap.heapSort(random_list)
        stop = timeit.default_timer()
        print("Sorted array:- ", end='\n')
        print(np.array2string(random_list, separator=', '))
        print(len(random_list), "Elements were sorted by Heap Sort in ", stop - start)
        h_elements.append(len(random_list))
        h_times.append(stop - start)
    print('\n')
    print("INSERTION SORT:-")
    for i in range(1, 5):
        n = int(input("Enter your large random number:- "))
        random_list = randint(0, n, n)
        print("Pseudo-Random Generated Array", end='\n')
        print(np.array2string(random_list, separator=', '))
        start = timeit.default_timer()
        insertion.InsertionSort(random_list)
        stop = timeit.default_timer()
        print("Sorted array:- ", end='\n')
        print(np.array2string(random_list, separator=', '))
        print(len(random_list), "Elements were sorted by Insertion Sort in ", stop - start)
        i_elements.append(len(random_list))
        i_times.append(stop - start)
    print('\n')
    plt.xlabel('Length')
    plt.ylabel('Time Complexity')
    plt.plot(m_elements, m_times, label='Merge Sort O(N log N)')
    plt.plot(h_elements, h_times, label='Heap Sort O(N log N)')
    plt.plot(i_elements, i_times, label='Insertion Sort O(N^2)')
    plt.plot(b_elements, b_times, label='Bubble Sort O(N^2)')
    plt.plot(s_elements, s_times, label='Selection Sort O(N^2)')
    plt.plot(q_elements, q_times, label='Quick Sort O(N log N)')
    plt.plot(qr_elements, qr_times, label='Quick Sort with 3 Medians O(N log N)')
    plt.grid()
    plt.legend()
    plt.gcf()
    plt.savefig('Sorting Graph.png', dpi=100)
    plt.show()