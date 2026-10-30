class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for char in s:
            if char in dic:
                stack.append(dic[char])
            else:
                if not stack or stack.pop() != char:
                    return False

        return not stack


        