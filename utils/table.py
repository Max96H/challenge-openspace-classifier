class Seat():
    """
    Class defining a seat wich can be occupied by one person only.
    """
    def __init__(self):
        """
        Constructor
        Takes no parameters
        self.free set to True and self.occupant set to an empty string.
        """
        self.free = True
        self.occupant = ""
    
    def set_occupant(self, name):
        """
        Method setting an occupant if free and changing the seat status
        :param: a string for the name of the would be occupant
        If not free: print who occupies the seat
        """
        if self.free:
            self.occupant = name.capitalize()
            self.free = False
        else:
            print(f"The seat is occupied by {self.occupant}")
    
    def remove_occupant(self):
        """
        Method setting the occupant back to an empty string and the seat status to free
        Takes no parameters
        Returns the name of the leaving occupant
        """
        leaving_occupant = self.occupant
        self.occupant = ""
        self.free = True
        return leaving_occupant
    
    def __str__(self):
        """
        Dunder method
        Return "An empty seat" or "Seat occupied by 'name'"
        """
        if self.free:
            return "An empy seat"
        return f"Seat occupied by {self.occupant}"

class Table():
    """
    Class defining a table with a limited capacity
    """
    def __init__(self, seats):
        """
        Constructor
        :param: an integer to set self.capacity
        self.seats set to a list of Seats() (lenght defined by capacity)
        """
        self.capacity = seats
        self.seats = [Seat() for _ in range(self.capacity)]
    
    def has_free_spot(self):
        """
        Boolean method checking if there is a least one empty seat
        """
        if any([seat.free for seat in self.seats]):
            return True
        return False
    
    def assign_seat(self, name):
        """
        Method filling a seat if any available.
        :param: a string for the would be occupant
        Prints to alert in case of a full table
        """
        if self.has_free_spot():
            for seat in self.seats:
                if seat.free:
                    seat.set_occupant(name)
                    break
        else:
            print("Sorry the table is full.")
    
    def left_capacity(self):
        """
        Method counting the number of empty seats
        Returns an integer
        """
        return sum([1 for seat in self.seats if seat.free])
    
    def __str__(self):
        """
        Dunder method
        Returns "A table with 'n' seats"
        """
        return f"A table with {self.capacity} seats"