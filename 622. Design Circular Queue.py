class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularQueue:
    """
    Design your implementation of the circular queue. The circular queue is a linear 
    data structure in which the operations are performed based on FIFO (First In First Out) 
    principle, and the last position is connected back to the first position to make a circle. 
    It is also called "Ring Buffer".

    One of the benefits of the circular queue is that we can make use of the spaces in front 
    of the queue. In a normal queue, once the queue becomes full, we cannot insert the next 
    element even if there is a space in front of the queue. But using the circular queue, 
    we can use the space to store new values.
    """

    def __init__(self, k: int):
        self.k = k
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.k <= self.count:
            return False
        new_node = Node(value)
        pre = self.tail.prev
        new_node.next, new_node.prev = self.tail, pre
        pre.next, self.tail.prev = new_node, new_node
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        remove = self.head.next
        self.head.next, remove.next.prev = remove.next, self.head
        self.count -= 1
        return True

    def Front(self) -> int:
        return self.head.next.val if self.head.next != self.tail else -1

    def Rear(self) -> int:
        return self.tail.prev.val if self.tail.prev != self.head else -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
