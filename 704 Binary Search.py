class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        length = len(nums)
        high = length - 1
        if ( low == high ):
            if(nums[low]==target):
                return low
            else:
                return -1
        else:
            while(low <= high):
                mid = low + (high - low)//2
                if(nums[mid] == target):
                    return mid
                elif(nums[mid] < target):
                    low = mid + 1
                elif(nums[mid] > target):
                    high = mid -1
            return -1

