def naive(arr, targetIndex):
    #loop from start by the next
    localMax = - float('inf')

    for num in arr[0 : targetIndex]:
        if num < targetIndex:
            localMax = max(localMax, num)

    return localMax


def smart(arr, targetIndex):
    #Is there any other fucking way other than this?

    # keep two array? Another one keep the local max of matching index.
    # if arr[index] > arr[i], and ans[i]
    # for i in range(targetIndex,0):


    return None