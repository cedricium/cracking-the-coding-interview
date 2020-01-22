def check_permutation(s1, s2):
    """Given two strings, write a method to decide if one is a permutation of
    the other.

    Args:
        s1 - first string
        s2 - second string
    Returns:
        bool - True if one string is a permutation of the other, False otherwise.
    """
    if len(s1) != len(s2):
        return False
    return True if sorted(s1) == sorted(s2) else False
