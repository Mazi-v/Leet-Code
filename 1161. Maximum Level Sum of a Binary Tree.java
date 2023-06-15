/*Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal. */
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
    public int maxLevelSum(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int maxSum = Integer.MIN_VALUE;
        int maxSumLevel = 1;
        int currLevel = 1;
        while (!q.isEmpty()) {
            int s = q.size();
            int currSum = 0;
            for (int i = 0; i < s; i++) {
                TreeNode curr = q.remove();
                currSum += curr.val;
                if (curr.right != null) {
                    q.add(curr.right);
                }
                if (curr.left != null) {
                    q.add(curr.left);
                }
            }

            if (currSum > maxSum) {
                maxSum = currSum;
                maxSumLevel = currLevel;
            }
            currLevel++;
        }

        return maxSumLevel;
    }
}