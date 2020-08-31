def search4vowels_precise(word):
    """Displaying the vowels found in the string"""
    vowels=set('aeiou')
    return vowels.intersection(set(word))
