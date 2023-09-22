/*Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.*/
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        // Create an array to store whether it's possible to break the string up to that
        // point.
        boolean[] result = new boolean[s.length() + 1];

        // Initialize the result for an empty string as true.
        result[0] = true;

        // Iterate through the string from the beginning.
        for (int i = 1; i < result.length; i++) {
            // Iterate through all possible substrings before the current position 'i'.
            for (int j = 0; j < i; j++) {
                // If it's possible to break the string up to position 'j' and the substring
                // from 'j' to 'i'
                // exists in the word dictionary, mark result[i] as true and break the loop.
                if (result[j] == true && wordDict.contains(s.substring(j, i))) {
                    result[i] = true;
                    break;
                }
            }
        }
        // The final value in the 'result' array indicates whether it's possible to
        // break the entire string.
        return result[result.length - 1];
    }
}