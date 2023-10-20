import csv

def load_file(filename: str = "") -> list:
    """ Opens a CSV file """
    data = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def get_values_more_30(column: str = "") -> bool:
    """ Returns true if the column contains wage more than 30 """
    col_result = False
    col_values = []
    index = COLS.index(column)

    for row in ROWS:
        col_values.append(row[index])

    for elem in col_values:
        if float(elem) > 30:
            col_result = True
            break

    return col_result 

def main():
    data = load_file(filename = "data/wages_by_education.csv")
    global COLS
    global ROWS

    COLS = data[0]
    ROWS = data[1:]

    #print(COLS)
    #print(ROWS)

    for col_index in range(len(COLS)):
        cols_result = get_values_more_30(COLS[col_index])
        if cols_result:
            print(COLS[col_index])

if __name__ == "__main__":
    main()