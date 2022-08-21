# Spelling-Bee

This project was created to help people with the game Spelling Bee by NY Times. There a multiple Python files that can be used for different purposes. The link to the website is https://www.nytimes.com/puzzles/spelling-bee

### main.py
This program creates a list with all the words that only consist of the letters given by the game but that haven't been confirmed to be accepted by the website by me yet. This program is designed to help eliminate words from word_list.txt, that contains far too many words. This way as many words as possible can be ruled out.

### generate_words.py
This program generates all the words from both word lists that only consist of the letters given by the game. The list also containes words that haven't been confirmed to be accepted by the website yet and might not be the answer.

### generate_confirmed_words.py
This program only gives out the words that have been confirmed to be accepted by the website. This way (hopefully) all words the program spits out are legitimate answer for the website.

### Word lists
The file "word_list.txt" contains all the words from the english dictionary that either haven't been tried out yet or have been confirmed to work on the website. Any words that have been tried out but weren't accepted as a legitimate answer have been removed from this list.
The file "word_list_confirmed.txt" only contains words that have been confirmed by me to be accepted on the website. To get this list, I almost daily play the free version of the game on the official website. In the free version, I unfortunately have a limited amount of words I can type in, which drastically reduces the words checked each day, but I still get a few words done each day.