class Solution:
    def twoSum(self, nums, target):
        A = ""
        for i in nums:
            for x in range(len(nums)):
                if i + nums[x] == target:
                    A =  [nums.index(nums[x]), nums.index(i)]
                    print(A)

ret = Solution().twoSum([2,7,11,15], 9)