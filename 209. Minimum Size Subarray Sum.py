from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None:
            return 0
        elif nums[0]>=target:
            return 1

        slow,fast=0,0
        n=2**32
        while fast<=len(nums)-1:
            total=sum(nums[slow:fast+1])
            if total>=target:
                n=min(len(nums[slow:fast+1]),n)
                slow+=1
            else:
                fast+=1
        return n if n!=2**32 else 0

S=Solution()
print(S.minSubArrayLen(7,[2,3,1,2,4,3]))

