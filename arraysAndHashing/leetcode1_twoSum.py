# Jan 05, 2024
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        explored = {}
        for i, val in enumerate(nums):
            missing = target - val
            if missing in explored:
                return [i, explored[missing]]
            else:
                explored[val] = i