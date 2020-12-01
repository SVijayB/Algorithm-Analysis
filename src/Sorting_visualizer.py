import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

if __name__ == "__main__":
    N = int(input("Enter number of terms to be sorted \n> "))
    L = int(input("Enter the lowest valued number \n> "))
    M = int(input("Enter the maximum valued number \n> "))
    print(N, "random integers from", L, "to", M, "will be considered")

    array = []
    for i in range(0,N):
        n = random.randint(L,M)
        array.append(n)

    print("""Select your sorting method (Enter a number from 1-5 corresponding to the sorting algorithm.)
    1) Bubble Sort.
    2) Insertion Sort.
    3) Merge Sort.
    4) Quick Sort.
    5) Selection Sort""") 
    choice = int(input("> "))

    if(choice == 1):
        title = "Bubble Sort"
        generator_fn = BubbleSort(array)
    if(choice == 2):
        title = "Insertion Sort"
        generator_fn = InsertionSort(array)
    if(choice == 3):
        title = "Merge Sort"
        generator_fn = MergeSort(array, 0, N - 1)
    if(choice == 4):
        title = "Quick Sort"
        generator_fn = QuickSort(array, 0, N - 1)
    if(choice == 5):
        title = "Selection Sort"
        generator_fn = SelectionSort(array)
    else:
        print("Incorrect choice")