"""You are given a 0-indexed array of positive integers tasks, representing tasks that need to be completed in order, where tasks[i] represents the type of the ith task.

You are also given a positive integer space, which represents the minimum number of days that must pass after the completion of a task before another task of the same type can be performed.

Each day, until all tasks have been completed, you must either:

Complete the next task from tasks, or Take a break. Return the minimum number of days needed to complete all tasks."""
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        lastSeen = {}
        day=0
        for i in range(len(tasks)):
            if tasks[i] not in lastSeen or lastSeen[tasks[i]]+space<day:
                lastSeen[tasks[i]]=day
            else: 
                day=lastSeen[tasks[i]]+space+1
                lastSeen[tasks[i]]=day
            day+=1    
            
        return day    
        