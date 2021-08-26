class PermutationII:
    def permuteUnique(self, nums):
        if not nums:
            return [[]]
        res, temp = [], []
        visited = [False for _ in range(len(nums))]
        nums.sort()
        self.dfs(res, temp, nums, visited)
        return res

    def dfs(self, res, temp, nums, visited):
        if len(temp) == len(nums):
            res.append(temp[:])
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0:
                continue
            # Visited is after tracing back, coz visited is set to False after dfs

            temp.append(nums[i])
            visited[i] = True
            self.dfs(res, temp, nums, visited)
            visited[i] = False
            temp.pop()

