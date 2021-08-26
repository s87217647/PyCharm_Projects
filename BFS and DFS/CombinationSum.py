class CombinationSum:
    # Can there be negative nums?
    # Are nums, target always valid?
    # It should be sorted, aye?
    def combinationSum(self, nums, target):
        if not nums or not target:
            return []
        temp, res, sum = [],[], 0
        self.dfs(nums, target, temp, res, sum, 0)
        return res

    def dfs(self, nums, target, temp, res, sum, index):
        if sum == target:
            res.append(temp[:]) # deep copy, keep it in the fucking heart
            return
        if sum > target:
            return

        for i in range(index, len(nums)):
            temp.append(nums[i])
            self.dfs(nums,target, temp, res, sum + nums[i], i)
            temp.pop()