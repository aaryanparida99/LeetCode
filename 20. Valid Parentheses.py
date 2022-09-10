class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_braces = set(["(", "[","{"])
        dict_braces = {
            "(" : ")",
            "[" : "]",
            "{" : "}",
                      }
        
        for char in s:
            if char in open_braces:
                stack.append(char)
            elif (stack and char == dict_braces[stack[-1]]):
                stack.pop()
            else:
                return False
        if stack == []:
            return True