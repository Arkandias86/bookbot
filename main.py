def print_file_contents(fileContents):
    print(fileContents)

def count_lines(fileContents):
    words = fileContents.split()
    return len(words)

def letter_frequency(fileContents):
    string_lower = fileContents.lower()
    letters_frequencies = {}
    for i in range(len(string_lower)):
        char = string_lower[i]
        if char in letters_frequencies:
            letters_frequencies[char] += 1
        else :
            letters_frequencies[char] = 1
    return letters_frequencies

def main():
    book_path = "./books/frankenstein.txt"
    with open(book_path) as f:
        fileContents = f.read()
        print(letter_frequency(fileContents))

if __name__ == "__main__":
    main()