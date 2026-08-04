class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        index=len(nums)-1
        sorted_arr=[-1]*len(nums)
        while left<=right:
            if abs(nums[left])<abs(nums[right]):
                sorted_arr[index]=nums[right]**2
                index-=1
                right-=1
            else:
                sorted_arr[index]=nums[left]**2
                index-=1
                left+=1
        return sorted_arr
