"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a list of tuples containing the sorted string and its original index
        sorted_strs_indices=[]
        for i in range(len(strs)):
            sorted_strs_indices.append(["".join(sorted(strs[i])),i])

        # Sort the list of tuples based on the sorted string
        sorted_strs_indices = sorted(sorted_strs_indices)

        # Initialize variables to track the current group of anagrams
        temp_group = [strs[sorted_strs_indices[0][1]]]
        result_groups = []
        previous_sorted_str = sorted_strs_indices[0][0]

        # Iterate through the sorted list and group anagrams
        for i in range(1, len(strs)):
            if previous_sorted_str == sorted_strs_indices[i][0]:
                temp_group.append(strs[sorted_strs_indices[i][1]])
            else:
                # Add the current group to the result and start a new group
                result_groups.append(temp_group)
                previous_sorted_str = sorted_strs_indices[i][0]
                temp_group = [strs[sorted_strs_indices[i][1]]]

        # Add the last group to the result
        result_groups.append(temp_group)
        return result_groups


            