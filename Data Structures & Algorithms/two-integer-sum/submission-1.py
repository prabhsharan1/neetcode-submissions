class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 
        To reduce the Time Complexity we would use hashmap by adding
        Val = 2,1,5,3 and Index = 0,1,2,3 and then using that to find
        the target
        video: https://www.youtube.com/watch?v=KLlXCFG5TnA
        """
        Map = {} # Hash Map to store the values idx: val

        for i, n in enumerate(nums):
            diff = target - n
            if diff in Map:
                return [Map[diff], i]
            Map[n] = i