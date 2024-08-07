from helper import d
# 2. Set Operations in Data Analysis


# Objective: The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.


# Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python function to remove duplicates and display the unique customer IDs.


# Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

#Expected Outcome: A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.
d()

customer_ids = ['C001', 'C002', 'C003', 'C002', 'C001','C004']
print(customer_ids)
set_ids = set(customer_ids) # type cast my list into a set to remove duplicate data
print(set_ids)


d()

# unique_customers = set(customer_ids)    
# print('The set: ', unique_customers)          <------ Skipping a step   
