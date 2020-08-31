def vowels_exsist_in_string(word):
    """ Finding if the vowels exsist in a string or not """
    vowels=set('aeiou')
    found=vowels.intersection(set(word))
    #Returning true or False via Boolean
    return bool(found)


