# Import the required module(s)
from typing import List

# Problem Statement: https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        :param nums: list containing digits
        :param target: integer value representing target sum to be produced
        :return: list containing index location of first and last numbers which sum up as target
        """
        # Loop over the elements of the input list
        for i in nums:
            # Find the index location of the first value
            first_num_index = nums.index(i)
            # Loop over the input list again, but excluding the index of first number
            for j in nums[first_num_index+1:]:
                # Check whether the element sum is equal to the target
                if i + j == target:
                    # Find the index of the second number, exclude the index of first number
                    second_num_index = nums.index(j, first_num_index+1)
                    # Create the output list
                    two_sum_list = [first_num_index, second_num_index]
                    print(f'Two num list: {two_sum_list}')
                    return two_sum_list
                else:
                    continue
        return []

if __name__ == "__main__":
    obj = Solution()
    # obj.twoSum(nums=[2, 7, 11, 15], target=9)
    # obj.twoSum(nums=[3, 2, 4], target=6)
    obj.twoSum(nums=[3, 3], target=6)
