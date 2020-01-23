def one_away(a, b):
    """There are three types of edits that can be performed on strings: insert a
    character, remove a character, or replace a character. Given two string,
    check if they are one edit (or zero edits) away.

    Args:
        a - first String
        b - second String
    Returns:
        bool - True if a and b are zero or one edits away in similarity, False
        otherwise
    """
    if a == b:
        return True
    if abs(len(a) - len(b)) >= 2:
        return False

    a_set = set(a)
    b_set = set(b)
    if abs(len(a_set) - len(b_set)) >= 2:
        return False

    return True
