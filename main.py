word_file = open("word_list.txt")
word_list = []

for word in word_file:
    word_list.append(word.strip())
word_file.close()

main_letter = input("Type in the main letter: ")
letters = []

for i in range(1, 7):
    letters.append(input("Type in a letter: "))

possible_words = []

for word in word_list:
    if not main_letter in word:
        word_list.remove(word)

def wordChoice(main_letter, letters, word):
    letters.append(main_letter)
    if not main_letter in word:
        return False
    for letter in word:
        if not letter in letters:
            return False
    return True

for word in word_list:
    if wordChoice(main_letter, letters, word):
        possible_words.append(word)

print(possible_words)
