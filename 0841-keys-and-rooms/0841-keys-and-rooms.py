class Solution:
    def canVisitAllRooms(self, rooms):
        def dfs(node):
            for neighbor in rooms[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
                    
        seen = {0}
        dfs(0)
        return len(seen) == len(rooms)