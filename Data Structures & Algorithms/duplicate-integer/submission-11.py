class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # unique_nums = set(nums)
        # return len(unique_nums) != len(nums)
        # time complexity: O(n)
        # space complexity: O(n)
        
        # setNums = {}
        # for num in nums:
        #     if num in setNums:
        #         return True
        #     else:
        #         setNums[num] = 1
        #     print(setNums)
        # return False
        # time complexity: O(n)
        # space complexity: O(n)

        # setNums = set()
        # for num in nums:
        #     if num in setNums:
        #         return True
        #     else:
        #         setNums.add(num)
        # return False
        # time complexity: O(n)
        # space complexity: O(n)

        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
        # time complexity: O(nlogn)
        # space complexity: O(1)