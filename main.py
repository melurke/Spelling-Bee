with open("word_list.txt", "r") as file:
    word_list = []
    for word in file:
        word_list.append(word.strip())

with open("word_list_confirmed.txt", "r") as file:
    word_list_confirmed = []
    for word in file:
        word_list_confirmed.append(word.strip())

main_letter = input("Type in the main letter: ")
letters = []

for i in range(6):
    letters.append(input(f"Type in the {i + 1}. letter: "))

possible_words = []

for word in word_list:
    if not main_letter in word:
        word_list.remove(word)

def WordChoice(main_letter, letters, word):
    letters.append(main_letter)
    if not main_letter in word:
        return False
    for letter in word:
        if not letter in letters:
            return False
    return True

def Main():
    for word in word_list:
        if WordChoice(main_letter, letters, word) and not word in word_list_confirmed:
            possible_words.append(word)

    print(possible_words)

if __name__ == "__main__":
    Main()