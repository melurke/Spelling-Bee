word_list = []
word_file = open("word_list_confirmed.txt","r")
for word in word_file:
    word_list.append(word.strip())
word_file.close()

word_list = list(dict.fromkeys(word_list))
word_list.sort()
words = ""
for word in word_list:
    words += word + "\n"
word_file = open("word_list_confirmed.txt","w")
word_file.write(words)
word_file.close()
