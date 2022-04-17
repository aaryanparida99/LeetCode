class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        l = len (numbers)
        i = 0
        j = l-1
        while(i<j):
            x = numbers[i] + numbers[j]
            if x < target:
                i = i+1
            if x > target:
                j =  j-1
            elif x == target:
                result.append(i+1)
                result.append(j+1)
                return result
