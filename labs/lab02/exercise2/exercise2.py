# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals
    tent_amount = math.ceil(participants / tent_capacity)
    cost_of_tent = tent_amount * tent_price
    cost_meal = meal_price * participants
    total_cost = cost_meal + cost_of_tent
    return total_cost
    

# Test your code here
print("Testing Camping Logistics...")
