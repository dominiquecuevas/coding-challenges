class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def make_bst(nums):
    if not nums:
        return
    mid = len(nums) // 2
    parent = BinaryNode(nums[mid])
    left_nums = nums[:mid]
    right_nums = nums[mid+1:]
    parent.left = make_bst(left_nums)
    parent.right = make_bst(right_nums)
    return parent

tree = make_bst([1,2,3,4,5,6,7])
"""
        4
     /-----\
    2      6
   / \    / \
  1   3  5   7
"""
print(f'Root node: {tree.data}')  
print(f'Root node left child: {tree.left.data}')
print(f'Root node left right child: {tree.left.right.data}')
print(f'Root node left left child: {tree.left.left.data}')

        
# def make_bst(nums):

#     if not nums:
#         return None
        
#     # if len(nums) == 1:
#     #     return nums[0]
    
#     parent_node_idx = len(nums)//2
#     parent_node = BinaryNode(nums[parent_node_idx])

#     parent_node.left = make_bst(nums[:parent_node_idx])
#     # parent_node.left = BinaryNode(left)
    
#     parent_node.right = make_bst(nums[parent_node_idx+1:])
#     # parent_node.right = BinaryNode(right)

#     return parent_node


