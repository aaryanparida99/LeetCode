class Solution:
    def reverse(self, x: int) -> int:
        temp , rev= 0, 0
        if x < 0 :
            tc = True
            x = x*-1
        else:
            tc = False
            
        while(x > 0):
            temp  = x % 10
            rev = rev * 10 + temp
            x = x//10
        if(tc):
            rev = rev * - 1
        if rev >= (2**31) - 1 or rev <= (-2**31):
            return 0
        else:
            return rev