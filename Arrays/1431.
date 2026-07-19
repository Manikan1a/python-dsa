class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        greatest=max(candies)
        for i in candies:
            i+=extraCandies
            if i>=greatest:
                result.append(True)
            else:
                result.append(False)
        return result
