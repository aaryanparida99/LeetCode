class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k > length :
            k = k - length
        nums[:] = nums[length - k :] + nums[ : length - k]