from collections import deque
class MovingAverage:
    def __init__(self, size):
        self.queue = collections.deque(maxlen=size)
        

    def next(self, val):
        queue = self.queue
        queue.append(val)
        return float(sum(queue))/len(queue)
        