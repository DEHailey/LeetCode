class Solution:
    def canVisitAllRooms(self, rooms):
        seen = {0}
        stack= [0]
        
        while stack:
            node = stack.pop()
            for neighbor in rooms[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        
        return len(seen) == len(rooms)