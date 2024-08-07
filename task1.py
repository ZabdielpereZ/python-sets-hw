from helper import d

# Task 1: Flight Route Comparison :
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# Destinations that both airlines fly to.  #Done

# Destinations unique to your airline.  #Done

# Whether there are any destinations that neither airline shares. #Done

# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

d()

same_path = our_routes.intersection(competitor_routes)
print(same_path)

d()

print(our_routes.difference(competitor_routes))
print(competitor_routes.difference(our_routes))

d()

diff_path = our_routes.symmetric_difference(competitor_routes)
print(diff_path)

d()