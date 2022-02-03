from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]
            if target == num:
                return mid
            elif target <= num:
                right = mid - 1
            else:
                left = mid + 1
        return -1


S = Solution()
print(S.search([-1, 0, 3, 5, 9, 12], 9))
