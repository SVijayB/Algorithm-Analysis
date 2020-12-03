import random
import time
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Modules.BubbleSort import BubbleSort
from Modules.InsertionSort import InsertionSort
from Modules.MergeSort import MergeSort
from Modules.QuickSort import QuickSort
from Modules.SelectionSort import SelectionSort
from Modules.Csv_writer import write
from Modules.Colours import *

if __name__ == "__main__":

    os.system('cls')
    logo = open("../assets/logo.txt","r")
    output = "".join(logo.readlines())
    grey(output)
    cyan("\n"+"-"*20)
    print()
    time.sleep(1)

    try:
        N = int(input("Enter number of integers to be sorted \n> "))
    except:
        red("ERROR : Enter only numbers!")
        grey("Press enter key to exit...")
        input()
        sys.exit(0)

    array = [x + 1 for x in range(N)]
    random.shuffle(array)
    data = array.copy()

    print()

    print("""Select your sorting method ->
(Enter a number from 1-5 corresponding to the sorting algorithm)
    1) Bubble Sort.
    2) Insertion Sort.
    3) Merge Sort.
    4) Quick Sort.
    5) Selection Sort""")
    try:
        choice = int(input("> "))
    except:
        red("ERROR : Enter numbers from 1 to 5 only!")
        grey("Press enter key to exit...")
        input()
        sys.exit(0)

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
        print()
        red("ERROR : Incorrect choice. Select numbers from 1 to 5 only!")
        grey("Press enter key to exit...")
        input()
        sys.exit(0)

    fig, axis = plt.subplots()
    axis.set_title(title)

    rect = axis.bar(range(N), array, align="edge")

    axis.set_xlim(0, N)
    axis.set_ylim(0, int(1.05 * N))

    text = axis.text(0.02, 0.95, "", transform=axis.transAxes)

    count = [0]
    def update(array, rect, count):
        for x, val in zip(rect, array):
            x.set_height(val)
        count[0] += 1
        text.set_text("# of operations: {}".format(count[0]))

    anim = animation.FuncAnimation(fig, func=update, fargs=(rect, count), 
    frames=generator_fn, interval=1, repeat=False)
    plt.show()

    write(title,data,count[0])