from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        You have a lock with 4 circular wheels, each numbered '0' to '9'.
        The lock starts at '0000'. A move consists of turning one wheel
        by one slot forward or backward (wrapping around between '0' and '9').

        Deadends are codes that stop the lock from turning. If the lock
        reaches any of these states, it becomes unusable.

        Given a target code, return the minimum number of moves required
        to reach it from '0000', or -1 if it is impossible.
        """
        deadends_set = set(deadends)

        if target == "0000":
            return 0
        if "0000" in deadends_set or target in deadends_set:
            return -1

        q = deque([("0000", 0)])
        visited = {"0000"}

        while q:
            curr, moves = q.popleft()
            for i in range(4):
                for val in (-1, 1):
                    new_digit = (int(curr[i]) + val) % 10
                    new_state = curr[:i] + str(new_digit) + curr[i + 1:]

                    if new_state in deadends_set or new_state in visited:
                        continue
                    if new_state == target:
                        return moves + 1

                    q.append((new_state, moves + 1))
                    visited.add(new_state)

        return -1
