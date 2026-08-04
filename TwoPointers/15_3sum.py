class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        target=0
        nums.sort()
        result=[]
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue #skipping the duplicates for i
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[left]+nums[right]==-nums[i]:
                    result.append([nums[left],nums[right],nums[i]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1 #ksipping the duplicates for left
                    while left<right and nums[right]==nums[right+1]:
                        right-=1 #skipping the duplicates for right
                elif nums[left]+nums[right]<-nums[i]:
                    left+=1
                elif nums[left]+nums[right]>-nums[i]:
                    right-=1
        return result
                

