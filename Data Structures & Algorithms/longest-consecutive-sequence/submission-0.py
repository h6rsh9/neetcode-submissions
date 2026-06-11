class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        count = 1
        max_count = 1
        new_nums = sorted(set(nums))
        for i in range(len(new_nums)-1):
            if new_nums[i+1] == new_nums[i]+1:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
        return max_count