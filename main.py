# ----------------------------------------
# Program that plays the game Spelling Bee from the NY Times by 
# going through a list of english words and finding the words 
# that only consist of 7 given letters
# ----------------------------------------

# Function to determine if a single given word fits the criteria given by the game
def WordChoice(main_letter, letters, word):
    letters.append(main_letter)
    if not main_letter in word:
        return False
    for letter in word:
        if not letter in letters:
            return False
    return True

# Function to write a list of words to a file at a given location
def WriteToFile(list, fileLocation):
    words = ""
    for word in list:
        words += word + "\n"
    with open(fileLocation, "w") as file:
        file.write(words)

# Main function
def Main():
    # Open files and generate the word lists
    with open("word_list.txt", "r") as file:
        wordList = []
        for word in file:
            wordList.append(word.strip())

    with open("word_list_confirmed.txt", "r") as file:
        wordListConfirmed = []
        for word in file:
            wordListConfirmed.append(word.strip())

    # Get the letters by input from the user
    mainLetter = input("Type in the main letter: ")
    letters = []

    for i in range(6):
        letters.append(input(f"Type in the {i + 1}. letter: "))

    possibleWords = []

    # Generate all possible words and print them out
    for word in wordList:
        if WordChoice(mainLetter, letters, word) and not word in wordListConfirmed:
            possibleWords.append(word)

    print("Possible Words:", possibleWords, "\n\n")

    # Go through all of the possible words and ask the player if the word was accepted by the site (to improve the list of words)
    for word in possibleWords:
        print(f"The current word is {word}")
        if not int(input("Can you input this word? ")):
            break
        isWord = int(input("Is the word correct? (1 or 0) "))
        print("")

        if isWord:
            wordListConfirmed.append(word)
        else:
            wordList.remove(word)

    # Remove duplicate words from the lists and sort them alphabetically
    wordList = list(dict.fromkeys(wordList))
    wordListConfirmed = list(dict.fromkeys(wordListConfirmed))
    wordList.sort()
    wordListConfirmed.sort()

    # Write the lists back to the files
    WriteToFile(wordList, "word_list.txt")
    WriteToFile(wordListConfirmed, "word_list_confirmed.txt")

# Run the main function
if __name__ == "__main__":
    Main()