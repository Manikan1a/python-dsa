class Solution:
    def compress(self, chars: list[str]) -> int:
        fast=0
        slow=0

        while fast<len(chars):
            current=chars[fast]
            count=0

            while fast<len(chars) and current==chars[fast]:
                fast+=1
                count+=1

            chars[slow]=current
            slow+=1

            if count>1:
                for digits in str(count):
                    chars[slow]=digits
                    slow+=1
        return slow
