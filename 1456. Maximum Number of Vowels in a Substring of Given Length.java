/*Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.*/

class Solution {
    public int maxVowels(String s, int k) {
        int start = 0;
        int result = 0;
        int count = 0;
        ArrayList<Character> vowels = new ArrayList<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        for (int end = 0; end < s.length(); end++) {
            count += vowels.contains(s.charAt(end)) ? 1 : 0;
            while (end >= start && k <= end - start) {
                count -= vowels.contains(s.charAt(start)) ? 1 : 0;
                start++;
            }
            result = Math.max(result, count);
        }
        return result;
    }
}