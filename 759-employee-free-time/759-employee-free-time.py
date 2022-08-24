"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
#operator.attrgetter(attr):Return a callable object that fetches attr from #its operand.
#heapq.merge(*iterables, key=None, reverse=False) Merge multiple sorted inputs into a single sorted output   
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        iterator = heapq.merge(*schedule, key=operator.attrgetter('start'))
        res, prev_end = [], next(iterator).end
        for event in iterator:
            if event.start > prev_end:
                res.append(Interval(prev_end,event.start))
            prev_end=max(prev_end,event.end)
        return res    
