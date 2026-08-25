class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set()
        for i in nums:
            ans.add(i)
        return len(ans) != len(nums)