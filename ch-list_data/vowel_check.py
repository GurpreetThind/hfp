vowels = ['a','e','i','o','u']

word1="bottle"
word2="nest"
word3="milkiway"

list_of_words = [word1, word2, word3]

for words in list_of_words:
    for letter in words:
        if letter in vowels:
            print(words, 'has vowel', letter )

