vowels = ['a','e','i','o','u']
 
word1="bottle"
word2="nest"
word3="milkiway"

list_of_words = [word1, word2, word3]

for words in list_of_words:
    for letter in words:
        if letter in vowels:
            print(words, 'has vowel', letter )

####################################################################

#print each found vowel only once
word1="bottle"
word2="nest"
word3="milkiway"

list_of_words = [word1, word2, word3]

found_vowels=[]

for words in list_of_words:
    for letter in words:
        if letter in vowels:
            if letter not in found_vowels:
                found_vowels.append(letter)

print(found_vowels)

for ch in found_vowels:
    print(ch)
#            print(words, 'has vowel', letter )
