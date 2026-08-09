"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        if not intervals:
            return True
        intervals = iter(intervals)
        prevInteval = next(intervals)
        for interval in intervals:
            if prevInteval.end > interval.start:
                return False
            prevInteval = interval      
        
        return True
