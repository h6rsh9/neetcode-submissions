class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0: 0, 1: 0, 2: 0}
        for num in nums:
            count[num] += 1

        index = 0
        for color in [0, 1, 2]:
            frequency = count[color]
            for _ in range(frequency):
                nums[index] = color
                index += 1