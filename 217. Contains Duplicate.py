class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l1 = len(nums)
        l2 = len(set(nums))
        if l1 == l2:
            return False
        return True