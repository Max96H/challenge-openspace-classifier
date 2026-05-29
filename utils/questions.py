def answering_qestions(open_space):
    """
    Function offering answers to three questions regarding the state of our openspace.
    :param: an Openspace object
    """
    counter = 0
    while (q:=input("\nIf you want the answer to any of these questions, type their number :\n1 How many seats are in the room?\n2 How many people are in the room?\n3 How many empty seats are left?\n4 No more questions, thank you\n--> ")) != "4" and counter < 7:
        counter += 1
        match q:
            case "1":
                print(f"\nThere are {open_space.number_of_tables * open_space.seats_per_table} seats total.")
            case "2":
                print(f"\nThere are {open_space.people_seated} people seated.")
            case "3":
                print(f"\nThere are {open_space.number_of_tables * open_space.seats_per_table - open_space.people_seated} empty seats left.")

    print("\nThank you, have a nice day.\n")