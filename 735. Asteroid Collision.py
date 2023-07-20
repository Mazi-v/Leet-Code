"""We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

"""
class Solution(object):
    def asteroidCollision(self, asteroids):
    
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        surviving_asteroids = []
        
        for current_asteroid in asteroids:
            # Check for possible collisions with the current asteroid and the top of the stack
            while surviving_asteroids and surviving_asteroids[-1] > 0 and current_asteroid < 0:
                if abs(surviving_asteroids[-1]) < abs(current_asteroid):
                    surviving_asteroids.pop()  
                elif abs(surviving_asteroids[-1]) == abs(current_asteroid):
                    surviving_asteroids.pop()  
                    break  
                else:
                    break  
            else:
                surviving_asteroids.append(current_asteroid)
        
        return surviving_asteroids