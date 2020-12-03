import random
import time
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Modules.BubbleSort import BubbleSort
from Modules.InsertionSort import InsertionSort
from Modules.MergeSort import MergeSort
from Modules.QuickSort import QuickSort
from Modules.SelectionSort import SelectionSort

if __name__ == "__main__":
    N = int(input("Enter number of terms to be sorted \n> "))

    array = [x + 1 for x in range(N)]
    random.shuffle(array)
    data = array.copy()

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

    temp = " "
    for x in data:
        temp = temp + str(x) + " "

    fields = ['Sorting Algorithm', 'List of numbers', 'Number of operations']

    try:
        open("Sorting_algorithm_data.csv","r")
    except:
         with open("Sorting_algorithm_data.csv","a+") as csvfile:
             writer = csv.DictWriter(csvfile, fieldnames = fields)
             writer.writeheader()

    with open("Sorting_algorithm_data.csv","a+") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
        value = [
            {'Sorting Algorithm':title, 'List of numbers':temp, 'Number of operations':count[0]}]
        writer.writerows(value)

    print("Data has been stored in the .CSV File.")
    input("Press enter key to exit")