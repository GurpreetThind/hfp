def serach_for_vowels(word):
    """ Return True or False if the Word contains a Vowel """
    vowels=set('aeiou')
    found=vowels.intersection(set(word))
    if len(found) == 0:
        return('False')
    else:
        return('True')
