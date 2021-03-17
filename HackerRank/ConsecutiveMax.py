class Solution:
    def findMaxConsecutiveOnes(nums):
        Max, List = 0, []
        for i in range(len(nums)):
            if nums[i] == 0:
                List.append(Max)
                Max = 0
            else:
                Max += 1
        List.append(Max)
        List.sort()
        print(List)


Solution.findMaxConsecutiveOnes([1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1])