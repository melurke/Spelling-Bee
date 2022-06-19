word_list = []

with open('word_list_confirmed.txt', 'r') as word_file:
    for word in word_file:
        word_list.append(word.strip())

word_list = list(dict.fromkeys(word_list))
word_list.sort()
words = ""
for word in word_list:
    words += word + "\n"

with open('word_list_confirmed.txt', 'w') as word_file:
    word_file.write(words)
