class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums + nums

        # nums.extend(nums)
        # return nums

        n = len(nums)
        result = [0] * 2 * n
        for i in range(n):
            result[i] = nums[i]
            result[i + n] = nums[i]
        return result
        # Time complexity: O(n)
        # Space complexity: O(n)