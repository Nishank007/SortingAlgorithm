import numpy as np
import random
from numpy.random import seed
from numpy.random import randint
import timeit
import matplotlib.pyplot as plt

from sort_module import selection
from sort_module import bubble
from sort_module import merge
from sort_module import insertion
from sort_module import quick
from sort_module import heap
from sort_module import quick_median_sort
from sort_module import graph

def menu():
    print(
        "Please Select the Sorting Algorithm:- \n 1.Merge Sort \n 2.Heap Sort \n 3.Quick Sort \n 4.Quick Sort with 3 Medians \n 5.Insertion Sort \n 6.Selection Sort \n 7.Bubble Sort \n 8.Comparison Graph ")
    choice = input("Enter your Choice:- ")
    print("\n")
    if choice == "1":
        n = int(input("Enter No. of Elements:- "))
        arr = input("Enter Numbers in the Array:- ")
        l = list(map(int, arr.split(' ')))
        print('Given Array is:- ',l)
        merge.mergeSort(l)
        print('Merge Sort Array is:- ',l)
    if choice == "2":
        n = int(input("Enter No. of Elements:- "))
        arr = input("Enter Numbers in the Array:- ")
        l = list(map(int, arr.split(' ')))
        print('Given Array is:- ', l)
        heap.heapSort(l)
        print('Heap Sort Array is:- ',l)
    if choice == "3":
        n = int(input("Enter No. of Elements:- "))
        arr = input("Enter Numbers in the Array:- ")
        alist = list(map(int, arr.split(' ')))
        print('Given Array is:- ',alist)
        quick.quicksort(alist, 0, len(alist))
        print('Quick Sort Array is:- ', end='')
        print(alist)
    if choice == "4":
        n = int(input("Enter No. of Elements:- "))
        arr = input("Enter Numbers in the Array:- ")
        l = list(map(int, arr.split(' ')))
        print('Given Array is:- ', l)
        quick_median_sort.quicksortmedian(l)
        print('Quick Sort with 3 Medians Array is:- ',l)
    if choice == "5":
        n = int(input("Enter No. of Elements:- "))
        arr = input("Enter Numbers in the Array:- ")
        l = list(map(int, arr.split(' ')))
        print('Given Array is:- ',l)
        insertion.InsertionSort(l)
        print('Insertion Sort Array is:- ',l)
    if choice == "6":
        n = int(input("Enter No. of Elements:- "))
        arr = input("Enter Numbers in the Array:- ")
        l = list(map(int, arr.split(' ')))
        print('Given Array is:- ',l)
        selection.selectionSort(l)
        print('Selection Sort Array is:- ',l)
    if choice == "7":
        n = int(input("Enter No. of Elements:- "))
        arr = input("Enter Numbers in the Array:- ")
        l = list(map(int, arr.split(' ')))
        print('Given Array is:- ',l)
        bubble.bubbleSort(l)
        print('Bubble Sort Array is:- ',l)
    if choice == "8":
        graph.graph()
print("\n")
menu()