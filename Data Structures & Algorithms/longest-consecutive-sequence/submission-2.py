class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums_set = set(nums)
        temp = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                temp = 1
                current = num
                while current + 1 in nums_set:
                    temp += 1
                    current += 1
            longest_streak = max(longest_streak,temp)
        return longest_streak

        