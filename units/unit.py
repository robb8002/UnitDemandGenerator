import sys
sys.path.append('../data')
import constants
# from constants import crisis_attrition_factor, conflict_attrition_factor

class Unit:
  # Base class for all units
    unit_size = None
    current_state = None
    # all_states = None
    attrition = None

    # constructor initialized the object into a known state with all its data
    def __init__(self, size, state):
        self.unit_size = size
        self.current_state = state
        # all_states = ["competition", "crisis", "conflict"]
        calculate_initial_attrition()

        # Basically, instead of having a whole buch of repetative code in your main.py, just so this
        # code once, assuming you pass in the right values into the __init__ method on object creation.
        # Add more functionality to this base class of any extended classes to adjust behavior of units.
        def calculate_initial_attrition():
            if self.current_state == "crisis":
                self.attrition = self.unit_size - (self.unit_size * constants.crisis_attrition_factor)
            elif self.current_state == "conflict":
                self.attrition = self.unit_size - (self.unit_size * constants.conflict_attrition_factor)
            else:
                self.attrition = 0
