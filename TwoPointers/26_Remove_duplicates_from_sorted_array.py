class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       if len(nums)==0:
        return 0
       slow=0
       for i in range(1,len(nums)):
        if nums[slow]==nums[i]:
            slow+=0
        else:
            slow+=1
            nums[slow]=nums[i]
       return slow+1
