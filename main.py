from utils.openspace import Openspace
from utils.file_utils import make_list_from_txt
import json

def main():
    """
    Main function of this project
    -Reads and takes in names from a text file 
    -Make use of an openspace
    -Organize the people(names) in the openspace by assigning one person per seat and randomly filling the tables
    -Write in an output text file the names of the people who found a seat in the openspace
    -Prints out the state of the openspace, one table at a time
    """
    input_filepath = "new_colleagues.txt"
    output_filename = "output.txt"

    with open("config.json") as jsfile:
        json_object = json.load(jsfile)


    choice = input("Pick the size of your openspace between 'small', 'medium' and 'large' : ")
    config = json_object[choice]

    names = make_list_from_txt(input_filepath)

    open_space = Openspace(config["tables"], config["seats_per_table"])

    open_space.organize(names)

    open_space.store(output_filename)

    open_space.display()

    answer = input("\nDid more people arrive late? (y/n) : ")
    if answer == "y":
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
    else:
        print("\nUnderstood, the seating is done")

    counter = 0
    while True:
        q = input("\nIf you want the answer to any of these questions, type there number :\n1 How many seats are in the room?\n2 How many people are in the room?\n3 How many empty seats are left?\n4 No more questions, thank you\n--> ")
        counter += 1
        if q == "1":
            print(f"There are {open_space.number_of_tables * open_space.seats_per_table} seats total.")
        elif q == "2":
            print(f"There are {open_space.people_seated} people seated.")
        elif q == "3":
            print(f"There are {open_space.number_of_tables * open_space.seats_per_table - open_space.people_seated} empty seats left.")
        elif q == "4" or counter >= 6:
            break

if __name__ == "__main__":
    main()
