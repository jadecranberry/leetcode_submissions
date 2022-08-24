class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        #Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            #find the max number n, eg. for [2, 3, 4], max would be 4
            max_number = max(max_number, num)
            
        @cache
        def max_points(num):
            #check for base cases
            if num==0:
                return 0
            if num==1:
                return points[1]
            
            #Apply recurrence relation
            return max(max_points(num-1), max_points(num-2)+points[num])
        
        return max_points(max_number) #max_points(n) top down