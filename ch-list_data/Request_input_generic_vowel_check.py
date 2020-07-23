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
word4="bottle"
word5="nest"
word6="milkiway"

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


##################################################################

#Generic word check Input request from user
word7=input("Please enter the word of your choice")
word8=input("Please enter the word of your choice")
word9=input("Please enter the word of your choice")
vowel_prompted=['a','e','i','o','u']
words_list_prompted = [word7, word8, word9]

found_vowel_prompted= []

for words_prompted in words_list_prompted:
    for charactr in words_prompted:
        if charactr in vowel_prompted:
            if charactr not in found_vowel_prompted:
                found_vowel_prompted.append(charactr)

for alphabet in found_vowel_prompted:
    print(alphabet)



