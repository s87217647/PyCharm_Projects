from typing import List
class Permutation:
    def permute(self, nums):
        if not nums:
            return [[]]
        res, temp = [], []
        visited = [False for _ in range(len(nums))]
        self.dfs(res, temp, nums, visited)
        return res

    def dfs(self, res, temp, nums, visited):
        if len(temp) == len(nums):
            res.append(temp[:])
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
            temp.append(nums[i])
            visited[i] = True
            self.dfs(res, temp, nums, visited)
            visited[i] = False
            temp.pop()
