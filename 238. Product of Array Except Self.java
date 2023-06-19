/*Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation. */
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];

        // Calculate products of elements to the left of each element
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                res[i] = 1; // Initialize the first element as 1
            } else {
                res[i] = res[i - 1] * nums[i - 1]; // Product of elements to the left
            }
        }

        int r = 1;

        // Calculate products of elements to the right of each element
        for (int i = nums.length - 2; i >= 0; i--) {
            r *= nums[i + 1]; // Accumulate the product of elements to the right
            res[i] *= r; // Multiply the product to the existing value in 'res'
        }

        return res;
    }
}
