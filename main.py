def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(words())
        print(characters())

def open_file():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        return f"{len(words)} words found in the document"

def sort_on(array):
    return array["occurances"]

def characters():
    open = open_file()
    lower = open.lower()
    unique = {}
    single_characters = list(lower)
    for single in single_characters:
        if single.isalpha():
            if single in unique:
                unique[single] += 1
            else:
                unique[single] = 1
    array = []
    for letter in unique:
        array.append({"letter": letter, "occurances": unique[letter]})
    array.sort(reverse=True, key=sort_on)
    for occurance in array:
        print(f"The '{occurance["letter"]}' character was found {occurance["occurances"]} times")

#characters()



main()
# words()
#amount = characters()
#print(amount)