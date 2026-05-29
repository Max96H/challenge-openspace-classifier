import json
from utils.file_utils import make_list_from_txt
from utils.late_arrivals import checking_late_arrivals
from utils.openspace import Openspace
from utils.preferances import make_relation_dict
from utils.questions import answering_qestions

def main():
    """
    Main function of this project
    """
    #Reads and takes in names from a text file
    input_filepath = "new_colleagues+.txt"
    names = make_list_from_txt(input_filepath)

    #Makes a 'whish list' in the form of a dictionnary
    wish_dict = make_relation_dict(names)

    output_filename = "output.txt"

    #Reads a json file containing the different configurations of openspaces
    with open("config.json") as jsfile:
        json_object = json.load(jsfile)

    #Offers a choice of configuration
    choice = input("Pick the size of your openspace between 'small', 'medium' and 'large' : ")
    config = json_object[choice]

    #Make use of an openspace
    open_space = Openspace(config["tables"], config["seats_per_table"])

    #Organize the people(names) in the openspace by assigning one person per seat and randomly filling the tables
    open_space.organize(names, wish_dict)

    #Write in an output text file the names of the people who found a seat in the openspace
    open_space.store(output_filename)

    #Prints out the state of the openspace, one table at a time
    open_space.display()

    #Check for late arrivals and eventually adds them
    checking_late_arrivals(open_space, output_filename)    

    #Answer some questions
    answering_qestions(open_space)

if __name__ == "__main__":
    main()
