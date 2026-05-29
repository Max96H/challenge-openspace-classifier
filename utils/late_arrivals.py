def checking_late_arrivals(open_space, output_filename):
    """
    Function for late arrivals in our openspace, find them a seat, update our output file and make a new display in the Terminal
    :param: An Openspace object
    :param: a string of a file
    """
    while input("\nDid more people arrive late? (y/n) : ") == "y":

            new_people = []

            try:
                n = int(input("How many people needs a seats ? "))
            except TypeError:
                n = int(input("Please write an integer with digits : "))
            for i in range(n):
                new_people.append(input(f"Name {i+1} : "))

            open_space.organize(new_people)
            open_space.store(output_filename)
            open_space.display()

    print("\nUnderstood, the seating is done")