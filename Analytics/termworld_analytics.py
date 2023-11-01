import json

def load_file(filename: str = "") -> dict:
    file = open(filename, "r")
    data = json.load(file)

    for item in data:
        print("Item: ", item)
        idx = data.index(item)
        print("idx: ", idx)
        id = {"#": idx + 1} # dictionary
        print("id: ", id)
        print("old data[idx]: ", data[idx])
        # merge dictionaries
        id.update(data[idx])
        print("new id dic: ", id)
        data[idx] = id
        print("new data[idx]: ", data[idx])

    return data

def main():
    global DATA
    DATA = load_file(filename = "data/data.json")

if __name__ == "__main__":
    main()