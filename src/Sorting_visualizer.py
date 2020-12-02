import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Modules.BubbleSort import BubbleSort

if __name__ == "__main__":
    N = int(input("Enter number of terms to be sorted \n> "))

    array = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(array)

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
    elif(choice == 2):
        title = "Insertion Sort"
        generator_fn = InsertionSort(array)
    elif(choice == 3):
        title = "Merge Sort"
        generator_fn = MergeSort(array, 0, N - 1)
    elif(choice == 4):
        title = "Quick Sort"
        generator_fn = QuickSort(array, 0, N - 1)
    elif(choice == 5):
        title = "Selection Sort"
        generator_fn = SelectionSort(array)
    else:
        print("Incorrect choice")