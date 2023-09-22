class Solution(object):
    def topKFrequent(self, words, k):
        cnt = Counter(words)
        heap = [(-freq, word) for word, freq in cnt.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]
        
        