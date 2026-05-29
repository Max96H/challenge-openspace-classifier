def make_relation_dict(names):
    """
    Function creating a dictionnary of relationships
    :param: a list of strings of names with potentially an added relationship
    Returns a disctionnary
    """
    relation_dict = {}
    for i, name in enumerate(names):
        if "+" in name:
            name, other_name = name.split(f" + ")
            relation_dict[name] = other_name
            names[i] = name

    return relation_dict