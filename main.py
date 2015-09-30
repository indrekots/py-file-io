import sys, csv, string
from collections import Counter

csv_rows = []

def main():
    file_names = sys.argv[1:]
    for name in file_names:
        try:
            process_file(name)
        except FileNotFoundError:
            print("%s does not exist" % name)

    write_csv()

def process_file(name):
    with open(name, 'r') as f:
        append_row(name, f)

def unique_words(text):
    text = text.lower()
    for c in string.punctuation:
        text = text.replace(c, "")
    return len(Counter(text))

def append_row(filename, file):
    csv_rows.append({"file_name": filename, "unique_words": unique_words(file.read())})

def write_csv():
    with open('output1.csv', 'w') as f:
        field_names = ["file_name", "unique_words"]
        writer = csv.DictWriter(f, field_names)
        writer.writerows(csv_rows)

if __name__ == "__main__":
    main()
