"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""

#O(n^2) -> Takes quadratic time
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        if 1 not in nums:
            return 1
        res=float('inf')
        for num in nums:
            if num>0 and (num+1<res) and ((num+1) not in nums):
                res=num+1
        return res

print(Solution().firstMissingPositive([3, 4, -1, 1]))  # 2
print(Solution().firstMissingPositive([1, 2, 0]))      # 3
print(Solution().firstMissingPositive([7, 8, 9, 11]))  # 1
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 1<=nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        for i in range(len(nums)):
            if (i+1)!=nums[i]:
                return (i+1)
        return (len(nums)+1)

print(Solution().firstMissingPositive([3, 4, -1, 1]))  # 2
print(Solution().firstMissingPositive([1, 2, 0]))      # 3
print(Solution().firstMissingPositive([7, 8, 9, 11]))  # 1
