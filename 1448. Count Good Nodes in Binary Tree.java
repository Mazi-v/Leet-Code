/* Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree. */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */

class Solution {
    // Recursive helper function to determine the count of good nodes
    public int goodNode(TreeNode root, int max, int count) {
        if (root == null) {
            return 0;
        }

        // Check if current node is good based on the maximum value encountered so far
        count = root.val >= max ? 1 : 0;

        // Recursively check the left and right subtrees, updating the maximum value
        // encountered
        count += goodNode(root.left, Math.max(max, root.val), count)
                + goodNode(root.right, Math.max(max, root.val), count);

        return count;
    }

    // Main function to calculate the number of good nodes
    public int goodNodes(TreeNode root) {
        return goodNode(root, root.val, 0);
    }
}