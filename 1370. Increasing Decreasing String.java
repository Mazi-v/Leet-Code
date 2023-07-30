/*You are given a string s. Reorder the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.*/
class Solution {
    public String sortString(String s) {
        int[] arr = new int[26];
        for (int i = 0; i < s.length(); i++) {
            arr[s.charAt(i) - 'a']++;
        }
        StringBuilder str = new StringBuilder();
        while (str.length() < s.length()) {
            System.out.println(str);
            for (int i = 0; i < 26; i++) {
                if (arr[i] > 0) {
                    str.append((char) ('a' + i));
                    arr[i]--;
                }
            }
            for (int j = 25; j >= 0; j--) {
                if (arr[j] > 0) {
                    str.append((char) ('a' + j));
                    arr[j]--;
                }
            }

        }

        return str.toString();
    }
}