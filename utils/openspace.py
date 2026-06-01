import random
from utils.table import Table

class Openspace():
    """
    Class defining an openspace with a limited capacity
    It assigns people to a random table
    """
    def __init__(self, tables, seats):
        """
        Constructor
        :param: an integer to set self.number_of_tables
        :param: an integer to set self.seats_per_table
        Sets self.tables to a list of Tables()  (lenght defined by number_of_tables)
        Sets an index to be used in the method organize() to 0
        Sets self.people_seated to 0
        """
        self.number_of_tables = tables
        self.seats_per_table = seats
        self.tables = [Table(seats) for _ in range(self.number_of_tables)]
        self.idx = 0
        self.people_seated = 0
    
    def organize(self, names, wish_dict={}):
        """
        Method to fill the openspace with a list of people randomly assigned to tables
        :param: a list of strings, ideally the names of the people to be sitted.
        Uses the "random" library to shuffle the list of names
        Tries to spread the people accross the tables relatively evenly while avoiding sitting someone alone
        Tries to assign friends at the same table
        If we reach full capacity, offers to add as many tables as needed
        """
        random.shuffle(names)

        for i, name in enumerate(names):
            seated = False

            #checking that it is not the last and delta of capacity with next Table
            if i != len(names) - 1 and self.tables[self.idx].left_capacity() + 2 <= self.tables[(self.idx + 1) % self.number_of_tables].left_capacity():
                #switching to the next table with modulo!
                self.idx = (self.idx + 1) % self.number_of_tables

            #for the last person, checking if the table is empty and trying to find a non-empty table
            elif i == len(names) - 1 and self.tables[self.idx].left_capacity() == self.tables[self.idx].capacity:
                for j, table in enumerate(self.tables):
                    if j != self.idx and 1 <= table.left_capacity() < table.capacity:
                        self.idx = j
                        break

           #if all tables are full
            if all([not table.has_free_spot() for table in self.tables]):
                answer = input("Openspace is full! Do you want to add a table? (y/n) : ")
                if answer == "y":
                    self.tables.append(Table(self.seats_per_table))
                    self.number_of_tables += 1
                    self.idx = self.number_of_tables - 1
                else:
                    print("Sorry, see you next time.")
                    break

            # changing if the table is full
            while not self.tables[self.idx].has_free_spot():
                self.idx = (self.idx + 1) % self.number_of_tables
                
            #Checking for preferance
            if name in wish_dict:
                friend = wish_dict[name]
                for j, table in enumerate(self.tables):
                    if friend in [seat.occupant for seat in table.seats]:
                        if table.has_free_spot():
                            self.tables[j].assign_seat(name)
                            seated = True
                        break

            self.people_seated += 1

            if not seated:
                self.tables[self.idx].assign_seat(name)


            
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
        Table by table
        :param: a string of the file name
        """
        with open(filename, "w") as file:
            text = ""
            for i, table in enumerate(self.tables):
                text += f"Table {i + 1} :\n"
                for seat in table.seats:
                    text += f"  - {seat.occupant if not seat.free else 'Free'}\n"
            file.write(text.strip("\n"))
        
    def __str__(self):
        """
        Dunder method
        Returns "An openspace made of 'n' tables"
        """
        return f"An openspace made of {self.number_of_tables} tables"
