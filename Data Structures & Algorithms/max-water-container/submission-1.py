class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        
        while left < right:
            area = (right - left) * (min(heights[left],heights[right]))
            if area > max_area:
                max_area = area
            if heights[left] < heights[right]:
                current_heights = heights[left]
                while left < right and heights[left] <= current_heights: 
                    left = left + 1
            else:
                current_heights = heights[right]
                while left < right and heights[right] <= current_heights:
                    right = right - 1
        return max_area

