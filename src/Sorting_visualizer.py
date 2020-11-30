import random
import time

if __name__ == "__main__":
    N = int(input("Enter number of terms to be sorted \n> "))
    L = int(input("Enter the lowest valued number \n> "))
    M = int(input("Enter the maximum valued number \n> "))
    print(N, "random integers from", L, "to", M, "will be considered")
    print("""Select your sorting method (Enter a number from 1-5 corresponding to the sorting algorithm.)
    1) Bubble Sort.
    2) Insertion Sort.
    3) Merge Sort.
    4) Quick Sort.
    5) Selection Sort""")
    choice = int(input())

    array = []

    for i in range(0,N):
        n = random.randint(L,M)
        array.append(n)
    print(array)