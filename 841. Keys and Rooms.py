"""There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise."""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque()
        visited_rooms = {0}
        total_visited = 1  # Starting from room 0
        # Adding keys from room 0 to the queue and marking as visited
        for key in rooms[0]:
            queue.append(key)
            visited_rooms.add(key)
            total_visited += 1
        
        # BFS traversal to visit rooms
        while queue:
            current_room = queue.popleft()
            if total_visited == len(rooms):
                return True  # All rooms visited
            for key in rooms[current_room]:
                if key not in visited_rooms:
                    visited_rooms.add(key)
                    total_visited += 1
                    queue.append(key)    
        
        return total_visited == len(rooms)