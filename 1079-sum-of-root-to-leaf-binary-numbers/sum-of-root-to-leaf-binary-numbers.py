# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.binarys = []

        def dfs(root, cur_binary):
            cur_binary = cur_binary + [str(root.val)]

            if not root.left and not root.right:
                self.binarys.append(cur_binary)
            else:
                if root.left:
                    dfs(root.left, cur_binary)
                if root.right:
                    dfs(root.right, cur_binary)
        
        dfs(root, [])
        
        ans = 0

        for i in self.binarys:
            num_string = "".join(i)
            decimal = int(num_string, 2)
            ans += decimal
        
        return ans
        