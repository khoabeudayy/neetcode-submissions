class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}

        for char in t:
            need[char] = need.get(char, 0) + 1
        required = len(need)
        formed = 0
        left = 0

        min_len = float("inf")
        start = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in need and window[char] == need[char]:
                formed += 1
            
            while formed == required:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        return s[start:start + min_len] if min_len != float("inf") else ""
                

