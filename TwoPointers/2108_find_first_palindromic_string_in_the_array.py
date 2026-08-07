class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for fast in words:
            left=0
            right=len(fast)-1
            while left<right:
                if fast[left]!=fast[right]:
                    break
                left+=1
                right-=1
            if left>=right:
                return fast
        return ""
