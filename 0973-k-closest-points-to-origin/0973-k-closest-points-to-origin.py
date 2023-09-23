class Solution(object):
    def kClosest(self, points, k):
        points.sort(key = lambda p: p[0]**2 + p[1]**2)
        return points[:k]
        