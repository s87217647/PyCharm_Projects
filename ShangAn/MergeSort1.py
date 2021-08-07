class MergeSort1:

    #under the template of Divide and Conquer

#It's a sorting algo after all
    def sort(self, A):
        temp = [0 for _ in range(len(A))]
        self.mergeSort(A, 0, len(A) - 1, temp)
        return temp


    def mergeSort(self, A, start, end, temp):
        if start >= end:
            return
        mid = (start + end) // 2
        self.mergeSort(A, start, mid, temp)
        self.mergeSort(A, mid + 1, end, temp)
        self.merge(A, start, mid, end, temp)

    def merge(self, A, start, mid, end, temp):
        left = start
        right = mid + 1
        index = start
        while left <= mid and right <= end:
            if A[left] < A[right]:
                temp[index] = A[left]
                index += 1
                left += 1
            else:
                temp[index] = A[right]
                index += 1
                right += 1

        while left <= mid:
            temp[index] = A[left]
            index += 1
            left += 1

        while right <= end:
            temp[index] = A[right]
            index += 1
            right += 1

        for index in range(start, end + 1):
            A[index] = temp[index]


            #Trying to re-write it for the first time. Have no merge's logic