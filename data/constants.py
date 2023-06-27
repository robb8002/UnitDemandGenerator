import random

# Just an example of a "data" file with "constants" - better would be a data file to import, maybe JSON?
crisis_attrition_factor = random.uniform(0.01, 0.1)
conflict_attrition_factor = random.uniform(1, 3)

# put all the "ClassOneVariables" from main.py into here, import this file wherever you need the "constants"
# Better yet, use the same inheritance scheme with polymorphism on the class of supply classes. See what
# variables and functionality are hte same, extract into a base class, then inheric your class-of-supply
# classes from it
