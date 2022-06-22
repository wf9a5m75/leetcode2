class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n)


    def helper(self, start, end):
        if start > end: # edge case, see exposition below
            return [None]

        all_trees = [] # list of all unique BSTs
        for curRootVal in range(start, end+1): # generate all roots using list [start, end]
			# recursively get list of subtrees less than curRoot (a BST must have left subtrees less than the root)
            all_left_subtrees = self.helper(start, curRootVal-1)

			# recursively get list of subtrees greater than curRoot (a BST must have right subtrees greater than the root)
            all_right_subtrees = self.helper(curRootVal+1, end)

            for left_subtree in all_left_subtrees:   # get each possible left subtree
                for right_subtree in all_right_subtrees: # get each possible right subtree
                    # create root node with each combination of left and right subtrees
                    curRoot = TreeNode(curRootVal)
                    curRoot.left = left_subtree
                    curRoot.right = right_subtree

					# curRoot is now the root of a BST
                    all_trees.append(curRoot)

        return all_trees
