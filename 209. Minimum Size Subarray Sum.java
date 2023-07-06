/*Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.*/
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int start = 0;
        int sum = 0;
        int res = Integer.MAX_VALUE;
        for (int end = 0; end < nums.length; end++) {
            sum += nums[end];
            while (target <= sum && start <= end) {
                res = Math.min(res, end - start + 1);
                sum -= nums[start];
                start++;
            }
        }
        return res == Integer.MAX_VALUE ? 0 : res;
    }
}