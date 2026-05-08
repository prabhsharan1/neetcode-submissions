class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## HashSet Approach time complexity O(n)
        # empty set to track the numbers we have seen
        seen = set()

        for n in nums:
            # check if the number is in our set
            if n in seen:
                return True
            # if not we add it to the set
            seen.add(n)
        # If we didn't got any duplicates return False
        return False

        # Space and Time complexity O(n)