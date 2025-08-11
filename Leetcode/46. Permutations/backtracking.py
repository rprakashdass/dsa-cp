"""
Time Complexity: O(n * n!)
    - n! permutations total
    - n time to copy each permutation
Space Complexity: O(n * n!)
    - n! permutations stored in result
    - recursion stack up to depth n
"""

class Solution:
    def _getPermutation(self, nums: List[int], i: int):
        if i == len(nums):
            self.result.append(nums[:])
            return

        # At index i, try each element from i to end by swapping it into position i
        for ind in range(i, len(nums)):
            nums[ind], nums[i] = nums[i], nums[ind]
            self._getPermutation(nums, i+1)
            nums[ind], nums[i] = nums[i], nums[ind]  # swap back to original position

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self._getPermutation(nums, 0)
        return self.result