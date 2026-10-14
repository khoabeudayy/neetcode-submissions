class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            count = [0] * 26

            for c in word:
                index = ord(c) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key not in group:
                group[key] = [word]
            else:
                group[key].append(word)

        return list(group.values())

        