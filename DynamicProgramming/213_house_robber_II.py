class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def helpfn(nums):
            prev1=0
            prev2=0
            for i in nums:
                curr=max(prev1,prev2+i)
                prev2=prev1
                prev1=curr
            return prev1
        return max(helpfn(nums[:-1]),helpfn(nums[1:]))
