def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    phrase = phrase.lower()
    dict = {}
    for vowel in vowels:
        vow_amount = phrase.count(vowel)
        if vow_amount > 0:
            dict.update({vowel: vow_amount})
    return dict