class FirstAndLastPosition:
    def searchRange(self, nums, target):
        index1 = self.firstIndex(nums, target)
        index2 = self.lastIndex(nums, target)
        if not index1 or not index2:
            return [-1, -1]

        return [index1, index2]

    def firstIndex(self, num, target):
        left, right = 0, len(num) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if num[mid] < target:
                left = mid
            elif num[mid] >= target:
                right = mid

        if num[left] == target:
            return left
        if num[right] == target:
            return right
        return None

    def lastIndex(self, num, target):
        left, right = 0, len(num) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if num[mid] <= target:
                left = mid
            elif num[mid] > target:
                right = mid

        if num[right] == target:
            return right
        if num[left] == target:
            return left
        return None


