def if_palindrome(word: str) -> bool:

    """Function that checks if any permutation of word is palindrome
        Function counts how many diffrent letters are in th word and checks if there are more than one odd amount of letters.

    Parameters
    ----------
    word : str
        A word chosen by user

    Returns
    -------
    bool
        True if any of permutations is palindrome , False if is not or if it's empty string

    Example
    -------
    >>> if_palindrome("N_word")
        False
    >>> if_palindrome("bob")
        True
    """

    if word == "":
        return False
    char_set = set(word.upper())
    odd_number = True
    for each in char_set:
        if word.upper().count(each) % 2 != 0 and odd_number:
            odd_number = False
        elif word.upper().count(each) % 2 != 0 and odd_number == False:
            return False
    return True
