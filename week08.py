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

def delete(node, value):
    if node is None:
        return None
    if value < node.data:
        node.left = delete(node.left, value)
    elif value > node.data:
        node.right = delete(node.right, value)
    else: # 삭제할 노드 발견
        if node.left == None:
            return node.right
        elif node.right == None:
            return node.left
    return node




if __name__ == "__main__":
    numbers  = [10, 15, 8, 3, 9, 14]
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
find_target = int(input("찾는 값 입력"))

if search(root, find_target):
    print(f"{find_target}을(를) 찾았습니다.")
else:
    print(f"{find_target}을(를) 찾지 못했습니다.")


del_target = int(input("삭제할 값 입력"))
root = delete(root, del_target)

post_order(root)
print()
in_order(root)
print()
pre_order(root)
print()