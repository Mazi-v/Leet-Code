/*Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row. */
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        List<List<Integer>> result = new ArrayList<>();

        // Add the first row of the triangle to the result
        result.add(triangle.get(0));

        // Store the previous row of the triangle
        List<Integer> pre = triangle.get(0);

        // Iterate through the remaining rows of the triangle
        for (int i = 1; i < triangle.size(); i++) {
            List<Integer> currList = triangle.get(i); // Current row of the triangle
            List<Integer> temp = new ArrayList<>(); // Temporary list to store the minimum path values

            // Iterate through each element in the current row
            for (int j = 0; j < currList.size(); j++) {
                int currValue = currList.get(j); // Current element in the current row

                // Calculate the minimum path value from the previous row
                int a = (j >= 0 && j < pre.size()) ? pre.get(j) : Integer.MAX_VALUE; // Value from the same column
                int b = (j - 1 >= 0 && j - 1 < pre.size()) ? pre.get(j - 1) : Integer.MAX_VALUE; // Value from the
                                                                                                 // previous column
                int pastValue = Math.min(a, b); // Minimum path value from the previous row
                // Add the minimum path value to the temporary list
                temp.add(pastValue + currValue);
            }

            // Update the previous row with the temporary list
            pre = temp;

            // Add the temporary list to the result
            result.add(temp);
        }

        // Get the last row of the result
        List<Integer> lastList = result.get(result.size() - 1);

        // Sort the last row in ascending order
        Collections.sort(lastList);

        // Return the minimum value from the last row, which represents the minimum
        // total path
        return lastList.get(0);
    }
}