"""
UNIT DEMAND GENERATOR FOR COMPETITION, CRISIS, AND CONFLICT CONTIUUM 
By: 2ndLt Jessi Lanum

PROBLEM: Realistic demand generation is neccessary for increasing realism for logistics-based wargames. 
PURPOSE: Provide realistic demand generation for each class of supply depending on unit size and state.
OBJECTIVE: Provide quantitative demand data output for logistics-based wargames.

LAST UPDATED: xx JUL 23

#NOTE
This one will be all classes of supply outputted for each state of existance.

INTERNAL PROBLEM: I dislike having so many variables defined, but I can't think of a slicker option...
SOLUTION: Attempting for the first time some tuple unpacking. 

FUTURE USEAGE THOUGHTS: If adding to a larger program, probably refactor to seperate program into multiple
files. This way all variables can be in their own variables.py file. Potentially refactor this in the end to
do this. Add one option for all classes per state, and then one class with all states.
"""
#IMPORTS
import numpy

#VARIABLES
"""
Unit Size
"""
platoon_size = 50
company_size = 400
mlr_size = 2000

"""
Class 1: Food
"""
class ClassOneVariables:
    #Usual Request Based on MAGTF Planning
    individual_mean = 3
    platoon_mean = platoon_size * individual_mean
    company_mean = company_size * individual_mean
    mlr_mean = mlr_size * individual_mean
    
    #Demand Inflation Factor Depending on Continuum State
    competition_inflation_factor = 1
    crisis_inflation_factor = 2
    conflict_inflation_factor = 3

    #Competition Mean Calculations
    competition_demand_mean_platoon = competition_inflation_factor * platoon_mean
    competition_demand_mean_company = competition_inflation_factor * company_mean
    competition_demand_mean_mlr = competition_inflation_factor * mlr_mean

    #Crisis Mean Calculations
    crisis_demand_mean_platoon = crisis_inflation_factor * platoon_mean
    crisis_demand_mean_company = crisis_inflation_factor * company_mean
    crisis_demand_mean_mlr = crisis_inflation_factor * mlr_mean

    #Conflict Mean Calculations
    conflict_demand_mean_platoon = conflict_inflation_factor * platoon_mean
    conflict_demand_mean_company = conflict_inflation_factor * company_mean
    conflict_demand_mean_mlr = conflict_inflation_factor * mlr_mean
    
    #Standard Deviations
    competition_demand_stdev, crisis_demand_stdev, conflict_demand_stdev = 1, 1, 1

"""
Class 2: Equipment
"""
"""
Class 3: Fuel
"""
"""
Class 5: Ammo
"""
"""
Class 6: Personal Items 
"""
"""
Class 7: Major End Items
"""
"""
Class 9: Repair Parts
"""
"""
Class 10: Non-Military Items
"""

#DEMAND GENERATION
"""
Break each into functions.
"""
#Competition
def competition_demand_generator():
    #Class One
    competition_class_one_demand_platoon = numpy.random.lognormal(ClassOneVariables.competition_demand_mean_platoon, ClassOneVariables.competition_demand_stdev)
    competition_class_one_demand_company = numpy.random.lognormal(ClassOneVariables.competition_demand_mean_company, ClassOneVariables.competition_demand_stdev)
    competition_class_one_demand_mlr = numpy.random.lognormal(ClassOneVariables.competition_demand_mean_mlr, ClassOneVariables.competition_demand_stdev)

    return competition_class_one_demand_platoon, competition_class_one_demand_company, competition_class_one_demand_mlr
    #Class Two

#Crisis
#conflict

print(competition_demand_generator())