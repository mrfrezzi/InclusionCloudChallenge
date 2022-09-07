class SportPlayer():
    
    generic_expected_bmi = 20
    
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Question 2 - Add code to the empty methods
    def player_card(self):
        return ('Fullname: {}, {}'.format(self.last,self.first))
 
    # Question 2 - Add code to the empty methods
    @classmethod
    def update_expected_bmi(cls, generic_expected_bmi):
        cls.generic_expected_bmi = generic_expected_bmi

# Question 2 - Create a derived class from the base class
class FootballPlayer(SportPlayer): 
    
    # Question 2 - Inherits all properties and methods from the base class
    # pass

    # Question 2 - Initialize the properties differently from the base class
    sport = 'football'

    def __init__(self, first, last):
        self.first = first
        self.last = last
                 
#Test 1
footballer = FootballPlayer('leonel', 'messi')
print(footballer.player_card())
print(help(FootballPlayer))

# Output

# Fullname: messi, leonel

# Help on class FootballPlayer in module __main__:

# class FootballPlayer(SportPlayer)
#  |  FootballPlayer(first, last)
#  |
#  |  # Question 2 - Create a derived class from the base class
#  |
#  |  Method resolution order:
#  |      FootballPlayer
#  |      SportPlayer
#  |      builtins.object
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, first, last)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |
#  |  sport = 'football'
#  |
#  |  ----------------------------------------------------------------------
#  |  Methods inherited from SportPlayer:
#  |
#  |  player_card(self)
#  |      # Question 2 - Add code to the empty methods
#  |
#  |  ----------------------------------------------------------------------
#  |  Class methods inherited from SportPlayer:
#  |
#  |  update_expected_bmi(generic_expected_bmi) from builtins.type
#  |      # Question 2 - Add code to the empty methods
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors inherited from SportPlayer:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes inherited from SportPlayer:
#  |
#  |  generic_expected_bmi = 20