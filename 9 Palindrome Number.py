class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string = str(x)
        rev = int(string[::-1])
        if rev == x:
            return True
        else:
            return False
        