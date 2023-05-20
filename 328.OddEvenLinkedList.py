class Solution(object):
    """
        Given the head of a singly linked list, group all the nodes with odd indices together followed by
        the nodes with even indices, and return the reordered list.
    """
    def oddEvenList(self, head):

        # Check if the list is empty or has only one or two nodes
        if not head or not head.next or not head.next.next:
            return head

        # Initialize pointers for odd and even nodes
        headO = head  # Head of odd nodes
        headOdd = head  # Current odd node
        headE = head.next  # Head of even nodes
        headEven = headE  # Current even node

        # Traverse the list and rearrange nodes
        head = head.next.next
        while head:
            # Link the current odd node to the next odd node
            headO.next = head
            headO = headO.next

            if head.next:
                # Link the current even node to the next even node
                head = head.next
                headE.next = head
                headE = headE.next

                # Move to the next odd node
                head = head.next
            else:
                # Reached the end of the list
                break

        # Terminate the even node list
        headE.next = None

        # Connect the odd and even node lists
        headO.next = headEven

        return headOdd