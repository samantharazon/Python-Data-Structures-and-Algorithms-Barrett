# https://gist.github.com/sudhanshuptl/298ba90f411e95a6b0cb46e4dbadb742

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.utility_insert(self.root, value)

    def utility_insert(self, curr_node, insert_val):
        if curr_node.value == insert_val:
            return 
        if insert_val < curr_node.value:
            if curr_node.left is None:
                curr_node.left = Node(insert_val)
            else:
                self.utility_insert(curr_node.left, insert_val)
        else:
            if curr_node.right is None:
                curr_node.right = Node(insert_val)
            else:
                self.utility_insert(curr_node.right, insert_val)
    
    def search(self, curr_node, search_val):
        if curr_node is None:
            print('value (',search_val , ') is NOT Found !')
            return False
        elif curr_node.value == search_val:
            print('value (=', search_val, ') is Found ')
            return True
        elif search_val < curr_node.value:
            self.search(curr_node.left, search_val)
        else:
            self.search(curr_node.right, search_val)
    
    # returns node
    def deleteNode(self, curr_node, delete_val):
        if curr_node is None:
            return curr_node
        if delete_val < curr_node.value:
            curr_node.left = self.deleteNode(curr_node.left, delete_val)
        elif delete_val > curr_node.value:
            curr_node.right = self.deleteNode(curr_node.right, delete_val)
        else: 
            # Node with only one child or no child
            if curr_node.left is None: 
                return curr_node.right
            elif curr_node.right is None:
                return curr_node.left
            # Node with two children:
            curr_node.value = self.minValue(curr_node.right) 
            curr_node.right = self.deleteNode(curr_node.right, curr_node.value) # delete node to prevent duplicates (try commenting this line & run to see behavior)  
        return curr_node
    
    def minValue(self, curr_node):
        while curr_node.left:   
            curr_node = curr_node.left    
        return curr_node.value 

    def inorder(self, curr_node): # Left, Root, Right
        if curr_node:
            self.inorder(curr_node.left)
            print(curr_node.value, ', ', end='')
            self.inorder(curr_node.right)

    def preorder(self, curr_node): # Root, Left, Right
        if curr_node:
            print(curr_node.value, ', ', end='')
            self.preorder(curr_node.left)
            self.preorder(curr_node.right)

    def postorder(self, curr_node): # Left, Right, Root
        if curr_node:
            self.postorder(curr_node.left)
            self.postorder(curr_node.right)
            print(curr_node.value, ', ', end='')                   

print("\n")
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
my_tree.insert(90)
my_tree.insert(68)
my_tree.insert(80)

my_tree.root.display()

print("\nINORDER")
my_tree.inorder(my_tree.root)
print("\nPREORDER")
my_tree.preorder(my_tree.root)
print("\nPOSTORDER")
my_tree.postorder(my_tree.root)
print("\n")

my_tree.search(my_tree.root, 27)
my_tree.search(my_tree.root, 17)

print("\nMin Value at root:", my_tree.minValue(my_tree.root))

print("\nDelete Node ( 76 )")
my_tree.root = my_tree.deleteNode(my_tree.root, 76)
my_tree.root.display()
print("\n")

print("\nDelete Node ( 82 )")
my_tree.root = my_tree.deleteNode(my_tree.root, 82)
my_tree.root.display()
print("\n")


print("\n----- Test: Insert to Empty Tree -----\n")
bst = BinarySearchTree()
result = bst.insert(5)
bst.root.display()

print("\n----- Test: Insert to Existing Tree -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
result = bst.insert(3)
bst.root.display()

print("\n----- Test: Insert Duplicate Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
result = bst.insert(5)
bst.root.display()

print("\n----- Test: Insert Greater Than Root -----\n")
bst = BinarySearchTree()
bst.insert(10)
result = bst.insert(15)
bst.root.display()

print("\n----- Test: Insert Less Than Root -----\n")
bst = BinarySearchTree()
bst.insert(10)
result = bst.insert(5)
bst.root.display()
