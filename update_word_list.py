def WriteToFile(list, fileLocation):
    words = ""
    for word in list:
        words += word + "\n"
    with open(fileLocation, "w") as file:
        file.write(words)

def Main():
    with open("word_list.txt", "r") as file:
        wordList = []
        for word in file:
            wordList.append(word.strip())

    with open("word_list_confirmed.txt", "r") as file:
        wordListConfirmed = []
        for word in file:
            wordListConfirmed.append(word.strip())

    for word in wordListConfirmed:
        if not word in wordList:
            wordList.append(word)
    
    wordList.sort()

    WriteToFile(wordList, "word_list.txt")

if __name__ == '__main__':
    Main()