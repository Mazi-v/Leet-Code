/*Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

*/
class Solution {
    private boolean containsAllCharacters(HashMap<Character, Integer> map, HashMap<Character, Integer> targetMap) {
        // Check if all characters in targetMap are present in map with the correct
        // count
        for (Map.Entry<Character, Integer> entry : targetMap.entrySet()) {
            Character key = entry.getKey();
            Integer targetCount = entry.getValue();
            if (map.containsKey(key)) {
                Integer count = map.get(key);
                if (count < targetCount) {
                    return false;
                }
            } else {
                return false;
            }
        }
        return true;
    }

    public String minWindow(String s, String t) {
        HashMap<Character, Integer> targetMap = new HashMap<>();
        HashMap<Character, Integer> charCountMap = new HashMap<>();
        StringBuilder window = new StringBuilder();
        String minWindow = "";
        int start = 0;

        // Prepare the target character count map
        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            targetMap.put(c, targetMap.getOrDefault(c, 0) + 1);
        }

        for (int end = 0; end < s.length(); end++) {
            char c = s.charAt(end);
            window.append(c);
            charCountMap.put(c, charCountMap.getOrDefault(c, 0) + 1);

            while (containsAllCharacters(charCountMap, targetMap)) {
                String currentWindow = window.toString();

                // Update the minimum window if necessary
                if (minWindow.length() == 0 || currentWindow.length() < minWindow.length()) {
                    minWindow = currentWindow;
                }

                // Shrink the window from the left side
                char leftChar = s.charAt(start);
                charCountMap.put(leftChar, charCountMap.get(leftChar) - 1);
                window.deleteCharAt(0);
                start++;
            }
        }

        return minWindow;
    }
}