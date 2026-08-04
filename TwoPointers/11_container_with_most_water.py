class Solution:
    def maxArea(self, height: List[int]) -> int:
        right=len(height)-1
        left=0
        max_area=0
        while left<right:
            curr_area=(right-left)*min(height[left],height[right])
            if curr_area>max_area:
                max_area=curr_area
                if height[left]>height[right]:
                    right-=1
                else:
                    left+=1
            elif curr_area<=max_area:
                if height[left]>height[right]:
                    right-=1
                else:
                    left+=1
        return max_area
