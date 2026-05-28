from utils.openspace import Openspace
from utils.file_utils import make_list_from_txt


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

    names = make_list_from_txt(input_filepath)

    open_space = Openspace()

    open_space.organize(names)

    open_space.store(output_filename)

    open_space.display()

if __name__ == "__main__":
    main()
