"""You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points."""
from heapq import heappop, heappush
from collections import defaultdict
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Build adjacency list with Manhattan distances between all point pairs
        points_map = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                points_map[i].append((dist, j))
                points_map[j].append((dist, i))

        heap = [(0, 0)]  # (dist, starting_point)
        cost = 0
        visited = set()

        while heap:
            distance, node = heappop(heap)
            if node not in visited:
                cost += distance
                visited.add(node)
                if len(visited) == len(points):
                    return cost
                for dist, neighbor in points_map[node]:
                    if neighbor not in visited:
                        heappush(heap, (dist, neighbor))

        return cost
