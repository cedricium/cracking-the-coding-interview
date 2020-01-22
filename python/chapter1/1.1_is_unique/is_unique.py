def is_unique(str):
    """Implement an algorithm to determine if a string has all unique characters.

    Args:
        str - String to test whether its characters are all unique.
    Returns:
        bool - True if str contains all unique characters, False otherwise.
    """
    s = set(str)
    return True if len(str) == len(s) else False
