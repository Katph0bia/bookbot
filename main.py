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
    print(counter)

# main()