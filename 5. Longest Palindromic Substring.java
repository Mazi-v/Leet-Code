class Solution {
    // Given a string s, return the longest palindromic substring in s.
    public String longestPalindrome(String s) {
        String result = "";
        int maxLen = 0;
        // Iterate over each character in the string
        for (int i = 0; i < s.length(); i++) {
            // Iterate over all possible substrings starting from the current character
            for (int j = i; j < s.length(); j++) {
                String temp = s.substring(i, j + 1);
                if (temp.length() > maxLen) {
                    if (checkPalindrome(temp)) { // Check if the substring is a palindrome
                        maxLen = temp.length();
                        result = temp; // Update the longest palindrome substring
                    }
                }
            }
        }

        return result;
    }

    // Function to check if a string is a palindrome
    public boolean checkPalindrome(String s) {
        int end = s.length() - 1;
        for (int start = 0; start <= end; start++) {
            if (s.charAt(start) != s.charAt(end)) {
                return false;
            }
            end--;
        }
        return true;
    }
}