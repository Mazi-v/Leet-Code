"""Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        root.val = 0  
        
        prev_level_total = 0
        prev_sibling_sums = [0]

        while q:
            size = len(q)
            level_total = 0
            sibling_sums = []
            for i in range(size):
                node = q.popleft()
                children_sum = 0
                if node.left:
                    q.append(node.left)
                    children_sum+=node.left.val

                if node.right:
                    q.append(node.right)
                    children_sum+=node.right.val
                if node.left and node.right: sibling_sums.extend([children_sum,children_sum])
                elif node.left or node.right: sibling_sums.extend([children_sum])
                level_total+=children_sum

                node.val = prev_level_total - prev_sibling_sums[i]
            prev_sibling_sums = sibling_sums.copy()
            prev_level_total = level_total
                
        return root


