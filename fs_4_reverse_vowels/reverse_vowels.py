def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    VOWELS = 'aeiouAEIOU'
    vowel_list = []
    new_word = ''
    for char in s:
        if char in VOWELS:
            vowel_list.append(char)
    for char in s:
        if char in VOWELS:
            char = vowel_list.pop()
        new_word += char

    return new_word
