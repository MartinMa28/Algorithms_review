class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        if self.isValidBST(root.left) and self.isValidBST(root.right):
            left_child = root.left
            right_child = root.right

            if left_child:
                while left_child.right:
                    left_child = left_child.right

            if right_child:
                while right_child.left:
                    right_child = right_child.left

            if left_child == None and right_child == None:
                return True
            elif left_child == None and right_child:
                if root.val < right_child.val:
                    return True
                else:
                    return False
            elif right_child == None and left_child:
                if root.val > left_child.val:
                    return True
                else:
                    return False
            elif root.val > left_child.val and root.val < right_child.val:
                # root should be greater than right-most left child
                # and should be less than left-most right child as well
                return True
        
        return False

            
                
if __name__ == "__main__":
    solu = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(1)
    n1.right = n2

    print(solu.isValidBST(n1))