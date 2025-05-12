def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end=" -> ")

def in_order(node):
    if node:
        in_order(node.left)
        print(node.data, end=' -> ')
        in_order(node.right)

def pre_order(node):
    if node:
        print(node.data, end=' -> ')
        pre_order(node.left)
        pre_order(node.right)

class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None: # first node
        return  new_node

    current = root
    while True: # second node ~ last node
        if value < current.data:
            if current.left is None:
                current.left = new_node
                break
            current = current.left # move
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right # move
    return root

def search(root, target):
    current = root
    while True:
        if target == current.data:
            return True
        elif target < current.data:
            if current.left is None:
                return False
            current = current.left
        else:
            if current.right is None:
                return False
            current = current.right


if __name__ == "__main__":
    numbers  = [10, 15, 8, 3, 9]
    # numbers = [10, 15, 8, 3, 9, 1, 7, 100]
    root = None

    # 1번 원소 부터 마지막 원소 까지
    for number in numbers:
        root = insert(root, number)

print("BST 구성 완료")

post_order(root)
print()
in_order(root)
print()
pre_order(root)

print()

# 찾는 값 입력
target = int(input("찾는 값 입력"))

if search(root, target):
    print(f"{target}을(를) 찾았습니다.")
else:
    print(f"{target}을(를) 찾지 못했습니다.")

