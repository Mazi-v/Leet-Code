class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int result = 0;
        for (int pile : piles) {
            result = Math.max(pile, result);
        }
        int start = 1;
        int end = result;
        while (start <= end) {
            int mid = (start + end) / 2;
            int currentSpeed = 0;
            for (int pile : piles) {
                currentSpeed += (Math.ceil((pile * 1.0) / mid));
            }
            if (currentSpeed <= h) {
                result = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return result;
    }
}