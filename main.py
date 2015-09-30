import sys, csv, string
from collections import Counter

output = {
    "unique_words": {"file_name": "output1.csv",
                     "field_names": ["file_name", "unique_words"],
                     "data": []},
    #{"file_name": "output2.csv", "field_names": ["word", "count"]}
}

def main():
    file_names = sys.argv[1:]
    for name in file_names:
        try:
            process_file(name)
        except FileNotFoundError:
            print("%s does not exist" % name)

    write_csv_files()

def process_file(name):
    with open(name, 'r') as f:
        append_unique_words(name, f)

def unique_words(text):
    text = text.lower()
    for c in string.punctuation:
        text = text.replace(c, "")
    return len(Counter(text))

def append_unique_words(filename, file):
    output["unique_words"]["data"].append({"file_name": filename, "unique_words": unique_words(file.read())})

def write_csv_files():
    for key in output.keys():
        output_type = output[key]
        with open(output_type["file_name"], 'w') as f:
            field_names = output_type["field_names"]
            writer = csv.DictWriter(f, field_names)
            writer.writeheader()
            writer.writerows(output_type["data"])

if __name__ == "__main__":
    main()
