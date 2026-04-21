# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0
        
#         left = self.maxDepth(root.left)
#         right = self.maxDepth(root.right)

#         return 1 + max(left, right)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append(root)
        maxLevel = 0

        while queue:
            queueLen = len(queue)

            for _ in range(queueLen):
                currNode = queue.popleft()
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            
            maxLevel += 1
        
        return maxLevel
"""
NOTE: ITS MAX DEPTH FROM THE ROOT
        DEPTH = # Of NODES along the path
Execution:

depth(1)
 ├─ depth(2)
 │   ├─ depth(None) = 0
 │   ├─ depth(None) = 0
 │   └─ return 1 + max(0,0) = 1
 │
 └─ depth(3)
     ├─ depth(4)
     │   ├─ depth(None) = 0
     │   ├─ depth(None) = 0
     │   └─ return 1 + max(0,0) = 1
     │
     ├─ depth(None) = 0
     └─ return 1 + max(1,0) = 2

Back to depth(1):
return 1 + max(1,2) = 3

Final Answer: 3
Longest path: 1 → 3 → 4
"""