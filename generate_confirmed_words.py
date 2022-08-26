with open("word_list_confirmed.txt", "r") as file:
    wordListConfirmed = []
    for word in file:
        wordListConfirmed.append(word.strip())

mainLetter = input("Main Letter: ")
letters = []

for i in range(6):
    letters.append(input(f"{i + 1}. Letter: "))

possibleWords = []

def WordChoice(main_letter, letters, word):
    letters.append(main_letter)
    if not main_letter in word:
        return False
    for letter in word:
        if not letter in letters:
            return False
    return True

def Main():
    for word in wordListConfirmed:
        if WordChoice(mainLetter, letters, word):
            possibleWords.append(word)

    print(possibleWords)

if __name__ == "__main__":
    Main()