def palindrome_permutation(str):
    """Given a string, checks whether or not it is a permutation of a palindrome.

    Args:
        str - String to check against
    Returns
        bool - True if str is a permutation of a palindrome, False otherwise.
    """
    if len(str) == 0:
        return True

    chars = {}
    for char in str:
        char = char.lower()
        if char != ' ':
            if chars.get(char) != None:
                chars[char] += 1
            else:
                chars[char] = 1

    unbalanced = 0
    for count in chars.values():
        if count % 2 != 0:
            unbalanced += 1
            if unbalanced > 1:
                return False

    return True
