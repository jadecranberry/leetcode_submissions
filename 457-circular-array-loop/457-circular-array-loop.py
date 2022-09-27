#use fast and slow pointers for detect the circle
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        #for each index in the array we check if there is a possibility of circles 
        for i in range(len(nums)):
            #use is_forward to detect the moving direction
            is_forward = nums[i]>=0
            slow, fast=i,i
            
            while True:
                slow = self.find_next_index(nums, is_forward, slow)
                fast = self.find_next_index(nums, is_forward, fast)
                #move fast forward an element further
                if (fast!=-1):
                    fast=self.find_next_index(nums, is_forward, fast)
                if slow==-1 or fast==-1 or slow==fast:
                    break
            
            if slow!=-1 and slow == fast:
                return True
        return False 

    def find_next_index(self, arr, is_forward, current_index):
        #check the current direction, if it's different from is_forward, return -1
        direction = arr[current_index]>=0
        
        if is_forward != direction:
            return -1
        
        next_index = (current_index+arr[current_index])%len(arr)
        #if the next element returns to itself, return -1
        if next_index == current_index:
            next_index = -1
            
        return next_index     
        