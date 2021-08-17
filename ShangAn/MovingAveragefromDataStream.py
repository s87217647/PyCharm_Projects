# 没什么必要照着API 做， 用老师上课给的模板，重点是 test case 流程
# 滑动窗口的模板

class MovingAverageFromDataStream:
    def __init__(self, size: int = 0):
        self.size = size

    def next(self, val: int) -> float:
        return 0.0

    def movingAvg(self, nums, k):
        start, end = 0, k
        while end < len(nums):
            avg = sum(nums[start:end]) / (end - start)
            print(avg)
            start += 1
            end += 1

