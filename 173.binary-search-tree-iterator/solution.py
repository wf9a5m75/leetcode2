from typing import List, Union, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"[{self.val}: {self.left}, {self.right}]"

def buildTree(treeVals: List[Union[int, str]]) -> TreeNode:
    if (len(treeVals) == 0) or (treeVals[0] == "null") or (treeVals[0] is None):
        return None

    root = TreeNode(treeVals.pop(0))
    parent = [[root]]
    depth = 0
    idx = 0
    row = []

    while(treeVals):
        val = treeVals.pop(0)
        if val == "null" or val is None:
            node = None
        else:
            node = TreeNode(val)

        if (idx % 2 == 0):
            parent[depth][idx // 2].left = node
        else:
            parent[depth][idx // 2].right = node
        idx += 1
        row.append(node)

        if (idx == (2**(depth + 1)) ):
            idx = 0
            depth += 1
            parent.append(row)
            row = []

    return root


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.idx = 0
        self.values = []
        stack = []
        while(root or stack):
            while(root):
                stack.append(root)
                root = root.left

            root = stack.pop()
            self.values.append(root.val)
            root = root.right

    def next(self) -> int:
        val = self.values[self.idx]
        self.idx += 1
        return val

    def hasNext(self) -> bool:
        return self.idx < len(self.values)


input = """
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
"""
lines = input.split("\n")
commands,data = eval(lines[1]), eval(lines[2].replace("null", "None"))

results = []
target = None
for i, cmd in enumerate(commands):
    if (cmd == "BSTIterator"):
        target = BSTIterator(buildTree(data[i][0]))
        results.append(None)
    elif cmd == "next":
        results.append(target.next())
    elif cmd == "hasNext":
        results.append(target.hasNext())

print(results)
