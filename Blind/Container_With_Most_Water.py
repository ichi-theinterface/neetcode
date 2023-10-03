from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_bar = 0
        right_bar = 1
        most_water = 0
        while left_bar < len(height) - 1:
            while right_bar < len(height):
                print(f"the left bar is at {left_bar} \nthe right bar is at {right_bar}\n\n")
                temp_water = (right_bar - left_bar) * (min(height[right_bar], height[left_bar]))
                if temp_water > most_water:
                    most_water = temp_water
                    print("updated the most water!")
                right_bar += 1
            left_bar += 1
            right_bar = left_bar + 1
        return most_water

height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
# height = [1,8,6]

solution = Solution()

print(solution.maxArea(height=height))