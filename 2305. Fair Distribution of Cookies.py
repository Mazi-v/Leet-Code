"""
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.
"""

class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        # Initialize the distribution array with zeros for each child
        dist = [0] * k

        # Call the recursive function to distribute the cookies and return the result
        return self.giveCookies(0, cookies, dist, k, k)
    
    def giveCookies(self, i, cookies, dist, k, zeros):
        # Base case 1: If there are more bags with zero cookies than remaining bags, return a large value
        if zeros > len(cookies) - i:
            return sys.maxint
        
        # Base case 2: If all bags have been considered, return the maximum value in the distribution array
        if i == len(cookies):
            return max(dist)
        
        # Initialize the minimum unfairness to a large value
        ans = sys.maxint
        
        # Iterate over each child
        for j in range(k):
            # If the child has not received any cookies yet, decrement the count of bags with zero cookies
            if dist[j] == 0:
                zeros -= 1
            
            # Add the current bag of cookies to the total of the current child
            dist[j] += cookies[i]
            
            # Recursively call the function to distribute the next bag of cookies
            # Update the minimum unfairness by taking the minimum between the current minimum and the result of the recursive call
            ans = min(ans, self.giveCookies(i + 1, cookies, dist, k, zeros))
            
            # Remove the current bag of cookies from the total of the current child
            dist[j] -= cookies[i]
            
            # If the child has no cookies left, increment the count of bags with zero cookies
            if dist[j] == 0:
                zeros += 1
        
        # Return the minimum unfairness
        return ans