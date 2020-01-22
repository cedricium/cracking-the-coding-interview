def urlify(str, length=None):
    """Write a method to replace all spaces with '%20'.

    Args:
        str - String whose spaces should be replaced by '%20'
        length - length of str minus any spaces padded at the beginning or end
    Returns:
        A string similar to str except whose spaces have been replaced.
    """
    return str.strip().replace(' ', '%20')
