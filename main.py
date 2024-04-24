def print_file_contents(fileContents):
    print(fileContents)

def count_lines(fileContents):
    words = fileContents.split()
    return len(words)

def letter_frequency(fileContents):
    string_lower = fileContents.lower()
    letters_frequencies = []
    for i in range(len(string_lower)):
        char = string_lower[i]
        if char.isalpha():
            dict_letter = get_a_dict(letters_frequencies, char)
            if dict_letter:
                dict_letter["number"] += 1
            else :
                letters_frequencies.append({"letter" : char, "number" : 1})
    letters_sorted = sorted(letters_frequencies, key=lambda x: x['number'], reverse=True)
    return letters_sorted

def get_a_dict(collection, letter):
   return next((item for item in collection if item["letter"] == letter), None)

def print_report(dicts):
    print("Report for the frequency of each letter starting:")
    print("-------------------------------------------------")
    for dict in dicts:
        print("The letter " + dict["letter"] + " appears " + str(dict["number"]) + " times")
    print("-------------------------------------------------")
    print("Report finished")

def main():
    book_path = "./books/frankenstein.txt"
    with open(book_path) as f:
        fileContents = f.read()
    print_report(letter_frequency(fileContents))

if __name__ == "__main__":
    main()