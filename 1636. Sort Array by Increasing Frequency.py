class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num] = 1
        res = sorted(nums, key=lambda x: (dict[x], -x))
        return res