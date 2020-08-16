def serach_for_vowels(word):
    """Displaying the vowels conatined in the Input String """
    vowels=set('aeiou')
    found=vowels.intersection(set(word))
    for char in found:
        print(char)
		
#serach_for_vowels('hitch-hicker')
