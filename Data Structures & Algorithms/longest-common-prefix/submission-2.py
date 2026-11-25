# import os
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # return os.path.commonprefix(strs)
        common = ""
        for n in range(len(min(strs, key = len))):
            for m in range(len(strs)):
                if strs[m][n] != strs[0][n]:
                    return common
            common += strs[0][n]
        return common