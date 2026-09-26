class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       if len(nums)==0:
        return 0
       slow=0
       for fast in range(len(nums)):
        if nums[slow]==nums[fast]:
            pass
        else:
            slow+=1
            nums[slow]=nums[fast]
       return slow+1
