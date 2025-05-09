"""You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1."""

from collections import defaultdict
from heapq import heappop, heappush
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph_map = defaultdict(list)

        for s, d, w in times:  # source, destination, weight
            graph_map[s].append((w, d))

        heap = [(0, k)]  # (time, node)
        visited = set()

        while heap:
            cost, node = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return cost
            for w, neighbor in graph_map[node]:
                if neighbor not in visited:
                    heappush(heap, (cost + w, neighbor))

        return -1
