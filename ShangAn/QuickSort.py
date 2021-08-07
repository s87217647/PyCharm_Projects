class QuickSort:
    # I like 1th and 4th modelty

    def sort(self, A):
        self.QuickSort(A, 0, len(A) - 1)

    # Pivot: All on the left are smaller than to the right6

    def QuickSort(self, A, start, end):
        mid = self.partition(A, start, end)
        self.QuickSort(A, start, mid - 1)
        self.QuickSort(A, mid + 1, end)

        return

    # Never saw this partition in any resources
    def partition(self, A, start, end):
        m, pivot = start, A[start]

        return 0

    def swap(self, A, i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
