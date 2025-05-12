from os import remove


class Node:
       def __init__(self, data, link=None):
           self.data = data
           self.link = link

class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)


    def remove(self, target):
        current = self.head
        # if self.head.data == target:
        if current.data == target:
            self.head = self.head.link
            current.link = None
            return
        previous = None
        while current:
            if current.data == target:
                previous.link = current.link
                current.link = None
            previous = current
            current = current.link


    def search(self, target):
        current = self.head
        while current:
            if target == current.data:
                return f"{target}을 찾았습니다"
            else:
                current = current.link
        return f"{target}은 링크드 리스트에 존재 하지 않습니다."


    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            next = current.link
            current.link = previous
            previous = current
            current = next
        self.head = previous


    def __str__(self):
        current = self.head
        out_texts = ""
        while current is not None:
            out_texts = out_texts + f"{current.data} -> "
            current = current.link
        return out_texts + "END"


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
print(ll.search(8), ll.search(-9), ll.search(10), sep = "\n")
# ll.remove(10)
# ll.remove(8)
ll.reverse_list()
print(ll)

