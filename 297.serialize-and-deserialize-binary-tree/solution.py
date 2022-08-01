import math
ceil = math.ceil

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"[{self.val}: {self.left}, {self.right}]"

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if (node):
                results.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                results.append("#")
        results = []
        helper(root)
        return ",".join(results)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper():
            val = next(vals)
            if (val == "#"):
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node

        vals = iter(data.split(","))
        return helper()



# tree = Codec().deserialize("1,#,2,#,3,#,#")
# print(tree)
# result = Codec().serialize(tree)
# #tree2 = Codec().deserialize(result)
# print(result)
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
