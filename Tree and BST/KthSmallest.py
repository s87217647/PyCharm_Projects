class KthSmallest:
    def kthSmallest(self, root, k):
        count = self.nodeCount(root.left)
        if count + 1 == k:
            return root.val
        if count + 1 > k:
            return self.nodeCount(root.left, k)
        else:
            return self.nodeCount(root.right, k - count - 1)



    def nodeCount(self, root):
        if not root:
            return 0
        return 1 + self.nodeCount(root.left) + self.nodeCount(root.right)

    #看老师的解体，只要数最左边的 node 个数数出来就好（这是最优解）
