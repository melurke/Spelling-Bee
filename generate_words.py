with open("word_list.txt", "r") as file:
    wordList = []
    for word in file:
        wordList.append(word.strip())

with open("word_list_confirmed.txt", "r") as file:
    wordListConfirmed = []
    for word in file:
        wordListConfirmed.append(word.strip())

mainLetter = input("Type in the main letter: ")
letters = []

for i in range(6):
    letters.append(input(f"Type in the {i + 1}. letter: "))

possibleWords = []

for word in wordList:
    if not mainLetter in word:
        wordList.remove(word)

def WordChoice(main_letter, letters, word):
    letters.append(main_letter)
    if not main_letter in word:
        return False
    for letter in word:
        if not letter in letters:
            return False
    return True

def Main():
    for word in wordList:
        if WordChoice(mainLetter, letters, word):
            possibleWords.append(word)

    print(possibleWords)

if __name__ == "__main__":
    Main()