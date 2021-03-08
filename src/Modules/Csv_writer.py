import csv
from Modules.Colours import *


def write(title, data, terms, count):

    temp = " "
    for x in data:
        temp = temp + str(x) + " "

    fields = [
        "Sorting Algorithm",
        "Number of terms",
        "List of numbers",
        "Number of operations",
    ]

    try:
        open("Sorting_algorithm_data.csv", "r")
    except:
        with open("Sorting_algorithm_data.csv", "a+") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()

    with open("Sorting_algorithm_data.csv", "a+") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        value = [
            {
                "Sorting Algorithm": title,
                "Number of terms": terms,
                "List of numbers": temp,
                "Number of operations": count,
            }
        ]
        writer.writerows(value)

    print()
    green("Data has been stored in the Sorting_algorithm_data.csv File!")
    grey("Press enter key to exit")
    input()
