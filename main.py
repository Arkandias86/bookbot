def print_file_contents(fileContents):
    print(fileContents)

def count_lines(fileContents):
    words = fileContents.split()
    return len(words)

def main():
    book_path = "./books/frankenstein.txt"
    with open(book_path) as f:
        fileContents = f.read()
        print(count_lines(fileContents))

if __name__ == "__main__":
    main()