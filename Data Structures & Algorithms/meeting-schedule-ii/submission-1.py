"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        sort by start time
        minHeap of endTime

        we start a meeting, we add the end time to the minHeap
        if startTime < minimum endTime: room is free. use it (pop the min time). add 
        '''

        minHeap = [] #meeting rooms being used 
        heapq.heapify(minHeap)

        rooms = 0

        intervals.sort(key = lambda i : i.start)

        for interval in intervals:
            if minHeap and interval.start >= minHeap[0]: #room is empty
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, interval.end)
            else:
                heapq.heappush(minHeap, interval.end)
            
            rooms = max(rooms, len(minHeap))
        
        return rooms

        