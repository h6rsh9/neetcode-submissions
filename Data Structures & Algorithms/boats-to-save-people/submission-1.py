class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        people.sort()
        res = 0

        while l <= r:
            res += 1
            remain = limit - people[r]
            r -= 1

            if l <= r and people[l] <= remain:
                l += 1
        return res
        