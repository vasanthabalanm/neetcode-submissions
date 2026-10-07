class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}

        for idx in range(len(nums)):
            cur = target - nums[idx]
            if cur in Map:
                return [Map[cur], idx]
            Map[nums[idx]] = idx
        return [-1, -1]
        