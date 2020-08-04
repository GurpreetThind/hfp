vowels={'a','e','i','o','u'}

words=input("Please enter your word here: ")

found=vowels.intersection(set(words))

for vowel in found:
    print(vowel)
