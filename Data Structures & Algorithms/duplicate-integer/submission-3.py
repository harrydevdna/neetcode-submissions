class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # unique_nums = set(nums)
        # return len(unique_nums) != len(nums)
        # time complexity = O(n)
        # space complexity = O(n)
        setNums = {}
        for num in nums:
            if num in setNums:
                return True
            else:
                setNums[num] = 1
        return False