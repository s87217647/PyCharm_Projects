class BinaryTreeTraversal:
    def preorderTraversal(self, root):
        stack, res = [], []
        stack.append(root)
        while stack:
            cur = stack.pop()
            if not cur:
                continue
            res.append(cur.val)
            stack.append(cur.left)
            stack.append(cur.right) # 下一轮 先 pop 出来 right, I see, mofo. This is not pop left!

        return res