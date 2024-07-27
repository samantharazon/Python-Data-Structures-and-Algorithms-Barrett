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

    def utility_insert(self, current_node, insert_value):
        if current_node.value == insert_value:
            return 
        if current_node.value > insert_value:
            if current_node.left is None:
                current_node.left = Node(insert_value)
            else:
                self.utility_insert(current_node.left, insert_value)
        else:
            if current_node.right is None:
                current_node.right = Node(insert_value)
            else:
                self.utility_insert(current_node.right, insert_value)
    
    def search(self, current_node, search_value):
        if current_node is None:
            print('value (',search_value , ') is Not Found !')
            return False
        elif current_node.value == search_value:
            print('value (=', search_value, ') is Found ')
            return True
        elif search_value < current_node.value:
            self.search(current_node.left, search_value)
        else:
            self.search(current_node.right, search_value)


print("\n")
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

my_tree.root.display()
print("\n")

my_tree.search(my_tree.root, 27)
my_tree.search(my_tree.root, 17)
print("\n")
