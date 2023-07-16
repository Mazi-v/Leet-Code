
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode mergedHead = new ListNode(0);
        ListNode mergedTail = mergedHead;
        
        // 'min' will track the current minimum node among the lists
        ListNode min = new ListNode(Integer.MAX_VALUE);
        int minIndex = 0;
        
        // Check if the input list is empty
        if (lists.length == 0) {
            return mergedHead.next; // Return an empty list
        }
        // 'count' will keep track of the number of lists that have been fully traversed
        int count = 0;
        
        // Loop until all the lists are fully traversed
        while (true) {
            // Traverse each list to find the current minimum node
            for (int i = 0; i < lists.length; i++) {
                ListNode curr = lists[i];
                // If the current list is already fully traversed, increment 'count'
                if (curr == null) {
                    count++;
                }
                // If 'count' is equal to the number of lists, all lists have been fully traversed, so we return the merged list
                if (count >= lists.length) {
                    return mergedHead.next;
                }
                // Update 'min' and 'minIndex' if we find a smaller node
                if (curr != null && curr.val < min.val) {
                    min = curr;
                    minIndex = i;
                }
            }
            
            // Add the current minimum node to the merged list
            mergedTail.next = min;
            mergedTail = mergedTail.next;
            // Reset 'count' and 'min' for the next iteration
            count = 0;
            min = new ListNode(Integer.MAX_VALUE);
            // Move to the next node in the list that contains the minimum node
            if (lists[minIndex] != null) {
                lists[minIndex] = lists[minIndex].next;
            }
        }
    }
}