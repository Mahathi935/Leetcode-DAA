def rob(self, nums):
        prev, cur = 0, 0
        for n in nums:
            prev, cur = cur, max(cur, prev+n)
        return cur