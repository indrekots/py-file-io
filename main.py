import sys
from collections import Counter

def main():
    files = sys.argv[1:]
    f = open('file2.txt', 'r')
    print(f.read())

def unique_words(text):
    return len(Counter(text))

if __name__ == "__main__":
    main()
