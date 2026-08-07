class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        right=len(s)-1
        vowels="aeiouAEIOU"
        s=list(s)
        while left<right:
            if not s[left] in vowels:
                left+=1
            elif not s[right] in vowels:
                right-=1
            else:
                curr=s[left]
                s[left]=s[right]
                s[right]=curr
                left+=1
                right-=1
        return "".join(s)
