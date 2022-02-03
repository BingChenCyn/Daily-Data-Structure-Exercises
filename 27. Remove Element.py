from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0 or (len(nums)==1 and nums[0]==val):
            return 0

        slow,fast=0,0
        while fast<len(nums)-1:
            print(slow, nums[slow], fast, nums[fast])
            if nums[fast]!=val:
                print(val,nums)
                nums[slow] = nums[fast]
                print('after',val, nums)
                slow+=1
            fast += 1
            print('after',slow, nums[slow-1], fast, nums[fast])
        return slow







S = Solution()
# print(S.removeElement([3,2,2,3],3))
print(S.removeElement([0,1,2,2,3,0,4,2],2))
