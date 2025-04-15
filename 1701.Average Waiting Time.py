"""There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
timei is the time needed to prepare the order of the ith customer.
When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted."""
from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wait = 0
        # Initialize current time to the arrival time of the first customer
        curr = customers[0][0]  
        
        for i in range(len(customers)):
            if curr > customers[i][0]: 
                # If the cook is still busy, customer has to wait
                total_wait += (curr - customers[i][0])
            else:
                # If the cook is idle, start at customer's arrival time
                curr = customers[i][0]
            
            curr += customers[i][1]  # Update current time after serving the customer
            total_wait += customers[i][1]  # Add the service time to the total waiting time
        
        return total_wait / len(customers)  
