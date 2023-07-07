/* A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times. */
class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        // We need to find the maximum number of consecutive 'T's or 'F's in the answer
        // key
        return Math.max(maxForT(answerKey, k, 'F'), maxForT(answerKey, k, 'T'));
    }

    // Helper method to calculate the maximum number of consecutive 'T's or 'F's
    private int maxForT(String s, int k, char c) {
        int changes = 0;
        int start = 0;
        int result = 0;

        for (int end = 0; end < s.length(); end++) {
            // If the current character is not equal to the target character,
            // increment the changes counter.
            if (s.charAt(end) != c) {
                changes++;
            }

            // If the number of changes exceeds the allowed limit (k),
            // move the start pointer to shrink the window until the changes
            // are within the limit again.
            while (changes > k) {
                // If the character at the start pointer is not equal to the target character,
                // decrement the changes counter.
                if (s.charAt(start) != c) {
                    changes--;
                }
                start++; // Move the start pointer to the right
            }

            // Calculate the length of the current consecutive sequence
            // and update the result if necessary.
            result = Math.max(result, end - start + 1);
        }

        return result;
    }
}