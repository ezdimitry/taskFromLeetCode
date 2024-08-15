from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_pos = 0
        for num in nums:
            if num != val:
                nums[insert_pos] = num
                insert_pos += 1
        return insert_pos


sol = Solution()
nums = [3, 2, 2, 3]
val = 3
k = sol.removeElement(nums, val)


print(k)
print(nums[:k])