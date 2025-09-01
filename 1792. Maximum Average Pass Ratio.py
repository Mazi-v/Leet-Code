from typing import List
import heapq
class Solution:
    """
    You are given a list of classes, where each class is represented as [passi, totali].
    passi: number of students that will pass the exam in the class.
    totali: total number of students in the class.

    You also have extraStudents brilliant students who can be assigned to any class and
    are guaranteed to pass. Assign them to maximize the average pass ratio across all classes.

    Return the maximum possible average pass ratio after assigning the extra students.
    """

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Max-heap based on the potential improvement of adding one student
        heap = []
        for passed, total in classes:
            improvement = (passed + 1) / (total + 1) - passed/total
            heapq.heappush(heap, (-improvement, passed, total))
        while heap and extraStudents>0:
            _, passed, total = heapq.heappop(heap)
            passed += 1
            total += 1
            extraStudents -= 1
            improvement = (passed + 1) / (total + 1) - passed/total
            heapq.heappush(heap, (-improvement, passed, total))
        res = 0
        for _, passed, total in heap:
            res += passed / total
        return res/len(classes)


        