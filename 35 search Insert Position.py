class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        length = len(nums)
        high = length - 1
        if(length == 1):
            if(nums[0] >= target):
                return 0
            else:
                return 1
        if(nums[high] < target):
            return length
        if(nums[low] > target):
            return 0
        while(low <= high):
            mid = low + (high-low)//2
            if(nums[mid] == target):
                return mid;
            elif(nums[mid] > target):
                if(nums[mid-1] < target):
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1
