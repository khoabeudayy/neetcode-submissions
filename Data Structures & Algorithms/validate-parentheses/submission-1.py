class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        
        stack = []

        for char in s:
            if char in dic.keys():
                stack.append(char)
            else:
                if not stack or dic[stack[-1]] != char:
                    return False
                
                stack.pop()
        return len(stack) == 0


        