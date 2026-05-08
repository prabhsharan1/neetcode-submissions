class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        # zip(nums, nums[1:]) pairs [num1, num2], [num2, num3]...
        for a, b in zip(nums, nums[1:]):
            if a == b:
                return True
        return False