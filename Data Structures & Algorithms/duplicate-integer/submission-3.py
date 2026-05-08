class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        # Arr is sorted so easy to check for duplicates
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                # Just compare the side by side elements
                return True
        return False

        # Time Complexity O(N log N)
        # Space Complexity O(1) or O(n)
        