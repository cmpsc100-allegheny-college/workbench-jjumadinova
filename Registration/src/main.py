import csv

from rich.table import Table
from rich.console import Console

"""
A people registration system to demonstrate:

* lists
* for loop iteration
* while loop iteration
* program design

This program serves as part of the Allegheny College CMPSC 100: Computational
Expression course.
"""

def load_file(filename: str = "") -> list:
    """ Opens a CSV file """
    data = []
    with open(filename, "r") as fh:
        reader = csv.reader(fh)
        for row in reader:
            data.append(row)
    return data

def save_file(filename: str = "data/registrants.csv") -> None:
    """ Saves a CSV file """
    data = [COLS] + ROWS
    with open(filename, "w") as fh:
        writer = csv.writer(fh, delimiter = ",")
        for row in data:
            writer.writerow(row)

def display_table(rows: list = []) -> None:
    """ Display table using rich library """
    table = Table(title="REGISTRATIONS")
    if not rows:
        rows = ROWS
    for col in COLS:
        table.add_column(col)
    for row in rows:
        row = [str(elem) for elem in row]
        table.add_row(*row)
    console = Console()
    console.print(table)

def display_results(rows: list = []) -> None:
    """ Pass filtered results to table display """
    if not rows:
        rows = ROWS
    for idx in range(len(ROWS)):
        ROWS[idx] = [str(elem) for elem in ROWS[idx]]
    display_table(rows = rows)

### new functions - start
def get_participant_info(row_num: int = 0) -> list:
    """ Get specific participant info"""
    return ROWS[row_num]

def get_col(column: str = "") -> list:
    """ Get contents of the column"""
    values = []
    idx = COLS.index(column)
    for row in ROWS:
        values.append(row[idx])
    return values

def min(column: str = "") -> int:
    """ Get minimum value in the column """
    minimum = 40
    values = get_col(column)
    for value in values:
        value = int(value)
        if value < minimum:
            minimum = value
    return minimum

def average(column: str = "") -> int:
    """ Computes the average of a column """
    total = 0
    idx = COLS.index(column)
    for row in ROWS:
        total += int(row[idx])
    return total / len(ROWS)

def get_freq(column: str = "") -> int:
    """ Get the most common number that appears in column """
    value = 0
    times = 0
    data = get_col(column)
    value = data[0] # mode
    count = data.count(data[0])
    for elem in data:
        times = data.count(elem)
        if times > count:
            value = elem

    return value

def main():
    # Menu
    print("REGISTRATION STATION", end = "\n\n")
    print("Choose from the following options:", end = "\n")
    print("1. Get participant information")
    print("2. Get minimum age")
    print("3. Get averages")
    print("4. Get most frequent age")
    print("5. Display all registrants")
    print("0. Exit")

    data = load_file("data/registrants.csv")
    global COLS
    global ROWS
    COLS = data[0]
    ROWS = data[1:]

    # Loop through
    while True:

        # Resolve menu
        choice = int(input("Choose an option by number: "))
        # If exit, well, exit
        if choice == 0:
            break
        elif choice == 1:
            id = int(input("Enter id to fetch: "))
            row = get_participant_info(id - 1)
            print(f"Fetched participant : {row}")
        elif choice == 2:
            column = "age"
            minimum = min(column)
            print(f"Minimum {column}: {minimum}")
        elif choice == 3:
            ave = average("age")
            print("Average age: ", ave)
        elif choice == 4:
            mode = get_freq("age")
            print("Most common age: ", mode)
        elif choice == 5:
            display_results()

if __name__ == "__main__":
    main()