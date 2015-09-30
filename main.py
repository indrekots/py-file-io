import sys
from collections import Counter

def main():
    csv_rows = []
    file_names = sys.argv[1:]
    for name in file_names:
        try:
            with open(name, 'r') as f:
                append_row(name, f, csv_rows)
        except FileNotFoundError:
            print("%s does not exist" % name)

    print(csv_rows)

def unique_words(text):
    return len(Counter(text))

def append_row(filename, file, rows):
    rows.append({"name": filename, "unique_words": unique_words(file.read())})

if __name__ == "__main__":
    main()
