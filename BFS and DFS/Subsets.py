from typing import List
class Subset:
    def subsets(self, nums):
        if not nums:
            return []
        res, temp = [],[]
        self.dfs(res, temp, 0, nums)
        return res

    def dfs(self, res, temp, index, nums):
        res.append(temp[:])
        for i in range(index, len(nums)):
            temp.append(nums[i])
            self.dfs(res, temp, i + 1, nums)
            temp.pop()