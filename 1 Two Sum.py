class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx= []
        l = len(nums)
        for i in range(0,l):
            for j in range(i+1,l):
                if(nums[i] + nums[j] == target):
                    idx.append(i)
                    idx.append(j)
        return idx