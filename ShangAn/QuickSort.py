# 同向双指针is not very intuitive，trying another way to solve the prob
# Note: next time, spend time on choosing a intuitive way to remember
# Todo: Write the code and debug it yourself 对向双指针
# And, 捷抄的答案，after all

class QuickSort:
    def sort(self, A):
        self.QuickSort(A, 0, len(A) - 1)

    # Pivot: All on the left are smaller than to the right

    def QuickSort(self, A, start, end):
        if start >= end:
            return

        mid = self.partition(A, start, end)
        self.QuickSort(A, start, mid - 1)
        self.QuickSort(A, mid + 1, end)


    def partition(self, A, start, end):
        pivot = A[start]
        i, j = start + 1, end
        while i <= j:
            while i <= j and A[i] <= pivot:
                i += 1

            while i <= j and A[j] > pivot:
                j -= 1

            if i > j:
                break

            self.swap(A, i, j)
            i += 1
            j -= 1

        A[start] = A[j]
        A[j] = pivot
        return j




    def swap(self, A, i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
