class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:               
                dict[num] += 1
        heap = []
        for key,value in dict.items():
            heapq.heappush(heap,(-value,key))
        result = heapq.heappop(heap)
        return result[1]
