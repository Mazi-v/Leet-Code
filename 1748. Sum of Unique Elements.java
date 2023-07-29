/*You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.*/

class Solution {
    public int sumOfUnique(int[] nums) {
        int sum = 0;
        int[] arr = new int[101];
        for (int i = 0; i < nums.length; i++) {
            arr[nums[i]]++;
            if (arr[nums[i]] == 1)
                sum += nums[i];
            else if (arr[nums[i]] == 2)
                sum -= nums[i];
        }
        return sum;

    }
}