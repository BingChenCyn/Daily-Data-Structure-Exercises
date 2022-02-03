from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        k = len(nums) - 1
        while left <= right:
            if nums[left] ** 2 <= nums[right] ** 2:
                result[k] = nums[right] ** 2
                k -= 1
                right -= 1
            else:
                result[k] = nums[left] ** 2
                k -= 1
                left += 1
        return result


S = Solution()
print(S.sortedSquares([-4, -1, 0, 3, 10]))
