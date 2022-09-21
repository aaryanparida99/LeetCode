class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return l
        i = 1
        while(i < l):
            if nums[i] == nums[i-1]:
                nums.pop(i)
                l -= 1
            else:
                i += 1
        return len(nums)
        