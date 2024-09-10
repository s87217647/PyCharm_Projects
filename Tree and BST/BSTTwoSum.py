class BSTTwoSum:
    def findTarget(self, root, target):
        l = []
        self.inorder(root, l)
        i, j = 0, len(l) - 1
        while i < j:
            if l[i] + l[j] == target:
                return True
            elif l[i] + l[j] < target:
                i += 1
            else:
                j -= 1




    def inorder(self, root, l):
        if not root:
            return
        self.inorder(root.left, l)
        l.append(root.val)
        self.inorder(root.right, l)