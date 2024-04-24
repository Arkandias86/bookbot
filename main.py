def print_file_contents(fileContents):
    print(fileContents)

def main():
    book_path = "./books/frankenstein.txt"
    with open(book_path) as f:
        fileContents = f.read()
        print_file_contents(fileContents)

if __name__ == "__main__":
    main()