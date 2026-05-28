def make_list_from_txt(filename):
    with open(filename) as file:
        res = file.read().split("\n")
    return res