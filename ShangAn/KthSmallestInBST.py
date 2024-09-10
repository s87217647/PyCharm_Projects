class KthSmallestInBST:
    def kthSmallest(self, root, k):
        cnt = self.countNode(root.left)
        if cnt + 1== k:
            return root.val



    def countNode(self, root):
        if not root:
            return 0
        return 1 + self.countNode(root.left) + self.countNode(root.right)