class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_value=0
        max_value=0
        for i in range(len(nums)):
            if nums[i]==0:
                current_value=0
            else:
                current_value+=1
                if current_value>max_value:
                    max_value=current_value
        return max_value
