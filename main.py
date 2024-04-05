#with open("books/frankenstein.txt") as f:
#    file_contents = f.read()
#    print(file_contents)

# Count the ammount of words in the frankenstein text!
with open("books/frankenstein.txt") as f:
    # 1) Split
    # 2) Count
    file_contents = f.read()
    words = file_contents.split()
    counter = 0
    for word in words:
        counter += 1
    print(f"This book has >>{counter}<< words.")

# Definition to count the occurence of letters in the book
def letter_count():
    # 1) Read book; 2) Dictionary; 3) Split Book; 4) Count Everything.
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        letters_dictionary =  {letter: 0 for letter in alphabet}

        for char in file_contents.lower():
            if char in alphabet:
                letters_dictionary[char] += 1
    return (letters_dictionary)
print (letter_count())


# main()