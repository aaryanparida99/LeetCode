class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        startidx = -1
        endidx = -1
        if(nums == None or len(nums)<0):
            return(startidx,endidx)
        
        
        end = len(nums) - 1
        start = 0 
        while(start <= end):
            mid = start + (end-start)//2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
            if(nums[mid]==target):
                startidx = mid
                

        end = len(nums) - 1
        start = 0               
        while(start <= end):
            mid = start + (end-start)//2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
            if(nums[mid]==target):
                endidx = mid
                
        return(startidx,endidx)
                
            
        

            
            
            
        