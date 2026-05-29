def make_list_from_txt(filename):
    """
    Function makes a list out of names stored in a file
    :param: a string of a file
    Returns a list
    """
    with open(filename) as file:
        res = file.read().splitlines()
    return res