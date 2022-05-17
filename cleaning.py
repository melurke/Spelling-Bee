def num_of_letters(word):
    letters = []
    for letter in word:
        if not letter in letters:
            letters.append(letter)
    return(len(letters))

file = open("word_list.txt","r")
word_list = file.readlines()
file.close()
print(len(word_list))

for i in range(0, len(word_list)):
    word_list[i] = word_list[i].strip()

word_list_new = []

for word in word_list:
    if num_of_letters(word) > 7:
        word_list_new.append(word)

for word in word_list_new:
    word_list.remove(word)

words = ""

for i in range(0, len(word_list)):
    word_list[i] = word_list[i] + "\n"
    words += word_list[i]

file = open("word_list.txt","w")
file.write(words)
file.close()
