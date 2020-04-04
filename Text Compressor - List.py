# File Name: Text Compressor - List.py
# Purpose: Program that compresses text, then recreates it using the compressed list
# Date: 2020-03-01
# Last modified: 2020-03-01
# Author: Josen Pottackal
# Copy right no copyright
# Version: 1.0

while True:
    print("This program will compress text, then recreate it using the compressed list\n")

    phrase = input("Enter phrase:\n")
    editPhrase = (phrase.split())  # users phrase split into a list of separate words.

    # Prints a list of singular words from within the users input
    singularWords = []
    [singularWords.append(x) for x in editPhrase if x not in singularWords]
    print("Singular words within phrase:", singularWords, "\n")

    # each value in "edit_phrase" is replaced with the value that it represents in "singular_words"
    positions = []
    [positions.append(singularWords.index(x) + 1) for x in editPhrase]
    print("Compression:", positions, "\n")

    # each value in "singular_words" is replaced with the value that it represents in "positions"
    recreatedPhrase = []
    for pos in positions:
        recreatedPhrase.append(singularWords[pos - 1])
    print("Decompression:", " ".join(recreatedPhrase), "\n")

    while True:
        answer = input("Would you like to restart the program?(yes/no):\n").lower()
        if answer in ("yes", "no"):  # if answer does not equal "yes" or "no", the program prints an error message.
            break
        print("Sorry I didn’t understand, please try again:\n")
    if answer == "yes":  # if answer equals "yes" the program restarts.
        continue
    else:
        print("End program\n")  # if answer equals "no" the program ends.
        break
