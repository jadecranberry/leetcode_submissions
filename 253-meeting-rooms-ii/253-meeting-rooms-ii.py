
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x[0])
        min_rooms=[]
        heapq.heappush(min_rooms, intervals[0][1])
        
        for interval in intervals[1:]:
            #if the start time of next interval is bigger than the earliest finish time of a previous meeting, free this meeting room
            if interval[0]>=min_rooms[0]:
                heapq.heappop(min_rooms)
            heapq.heappush(min_rooms, interval[1])
            
        return len(min_rooms)    
    