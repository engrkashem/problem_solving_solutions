class Solution(object):
    def inorderTraversal(self, root):
        ans = []

        def inorder(treeNode):
            if treeNode:
                inorder(treeNode.left)

                ans.append(treeNode.val)

                inorder(treeNode.right)

        inorder(root)

        return ans
