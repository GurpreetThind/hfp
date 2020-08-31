def search4vowels(word:str)->set:
    """ Find all vowels in th string """
    vowels=set('aeiou')
    return vowels.intersection(set(word))
