"""Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times."""

 
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counter = Counter(citations)  # Count the number of citations for each value

        def findHindex(s: int, e: int, citations: List[int]):
            m = (s + e) // 2  # Calculate the midpoint

            if s > e:
                return m  # Return the current h-index if the search range is empty

            count = {x: c for x, c in citations.items() if x >= m}  # Count papers with citations greater than or equal to m

            if sum(count.values()) >= m:
                # If the count of papers with citations greater than or equal to m is greater than or equal to m,
                # it means that the researcher has published at least h papers that have each been cited at least h times,
                # so we search in the right half of the range.
                return findHindex(m + 1, e, citations)
            else:
                # Otherwise, we search in the left half of the range.
                return findHindex(s, m - 1, citations)

        return findHindex(0, len(citations), counter)