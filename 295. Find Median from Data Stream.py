"""The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 """
class MedianFinder:
    def __init__(self):
        # Max heap to store smaller half of numbers
        self.small = [] 

        # Min heap to store larger half of numbers
        self.large = [] 

    def addNum(self, num: int) -> None:
        # Push the negative value to simulate max heap
        heappush(self.small, -1 * num)

        # Balance heaps if necessary
        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            # If the max heap's top element is greater than the min heap's top element,
            # balance the heaps by moving an element from the max heap to the min heap
            heappush(self.large, -1 * heappop(self.small))

        # Adjust sizes to keep the heaps balanced
        if len(self.small) > len(self.large) + 1:
            # If the max heap's size is more than 1 larger than the min heap's size,
            # rebalance by moving an element from the max heap to the min heap
            heappush(self.large, -1 * heappop(self.small))
        if len(self.small) + 1 < len(self.large):
            # If the min heap's size is more than 1 larger than the max heap's size,
            # rebalance by moving an element from the min heap to the max heap
            heappush(self.small, -1 * heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # If the max heap has more elements, return its top element (negated)
            return -1 * self.small[0]
        if len(self.small) < len(self.large):
            # If the min heap has more elements, return its top element
            return self.large[0]
        # If both heaps have the same number of elements, calculate median
        return (-1 * self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()