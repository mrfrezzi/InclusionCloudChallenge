# Question 1 - Create a base class
class SportPlayer():
    
    # Question 1 - Three properties initialized at construction
    generic_expected_bmi = 20
    
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Question 1 - One empty instance method
    def player_card(self):
        pass

    # Question 1 - One empty class method    
    @classmethod
    def update_expected_bmi(cls):
        pass

                 
#Validation
sportman = SportPlayer('leonel', 'messi')
print(help(SportPlayer))

# Output
# Help on class SportPlayer in module __main__:

# class SportPlayer(builtins.object)
#  |  SportPlayer(first, last)
#  |  
#  |  # Question 1 - Create a base class
#  |  
#  |  Methods defined here:
#  |  
#  |  __init__(self, first, last)
#  |      Initialize self.  See help(type(self)) for accurate signatures.
#  |  
#  |  player_card(self)
#  |      # Question 1 - One empty instance method
#  |  
#  |  ----------------------------------------------------------------------
#  |  Class methods defined here:
#  |  
#  |  update_expected_bmi() from builtins.type
#  |      # Question 1 - One empty class method
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |  
#  |  generic_expected_bmi = 20