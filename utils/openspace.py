import random
from utils.table import Table

class Openspace():
    """
    Class defining an openspace with a limited capacity
    It assigns people to a random table
    """
    def __init__(self):
        """
        Constructor with 0 parameters
        Set self.number_of_tables to 6
        Set self.tables to a list of Tables()  (lenght defined by number_of_tables)
        """
        self.number_of_tables = 6
        self.tables = [Table() for _ in range(self.number_of_tables)]
    
    def organize(self, names):
        """
        Method to fill the openspace with a list of people randomly assigned to tables as long as there is empty seats
        :param: a list of strings, ideally the names of the people to be sitted.
        Uses the "random" library to choose a table, will keep looking if the table is full
        Prints to alert if the openspace is at full capacity.
        """
        for name in names:
            print(name)
            table = random.randint(0, self.number_of_tables-1)
            while not self.tables[table].has_free_spot():
                table = random.randint(0, self.number_of_tables-1)
                if all([not table.has_free_spot() for table in self.tables]):
                    print("Open space is full!")
                    break
            else:
                self.tables[table].assign_seat(name)
                continue
            break
    
    def display(self):
        """
        Method to nicely show the state of the openspace
        Goes table by table and prints out the names of occupants.
        """
        for i, table in enumerate(self.tables):
            print(f"\nTable {i + 1}:")
            for seat in table.seats:
                print(f"  - {seat.occupant}")
    
    def store(self, filename):
        """
        Method writing in a text file all the names of the occupants.
        One name per line
        :param: a string of the file name
        """
        with open(filename, "w") as file:
            file.write("\n".join(["\n".join([seat.occupant for seat in table.seats]) for table in self.tables]))
        
    def __str__(self):
        """
        Dunder method
        Returns "An openspace made of 'n' tables"
        """
        return f"An openspace made of {self.number_of_tables} tables"
