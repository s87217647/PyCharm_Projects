class ThreeSumClosest:
    # 3 sum 变形， 只不过判定变成是不是最小
    # 抄写
    def threeSumClosest(self, num, target) -> int:
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):# Mark this, coz it's different from 2 sum
            left, right = i + 1, len(num) - 1
            while left < right:
                sum = num[i] + num[left] + num[right]

                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):  #abs return difference between two  nums regardless order
                    target = sum

                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1

        return result

    # 回来再写一遍