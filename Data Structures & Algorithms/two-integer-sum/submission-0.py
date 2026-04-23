class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap: dict = {}

        for i, n in enumerate(nums):
            difference: int = target - n
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[n] = i
        return